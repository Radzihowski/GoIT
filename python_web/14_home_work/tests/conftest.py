import os
import importlib.util
import asyncio
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi_limiter import FastAPILimiter
from unittest.mock import AsyncMock, patch

from main import app
from src.database.models import Base
from src.database.db import get_async_session, DatabaseSessionManager
from src.repository import users as repository_users


TEST_DB_FILE = "./test.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{TEST_DB_FILE}"
SQLALCHEMY_ASYNC_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def _has_aiosqlite() -> bool:
    return importlib.util.find_spec("aiosqlite") is not None


@pytest.fixture(scope="session", autouse=True)
def prepare_test_db_file():
    if os.path.exists(TEST_DB_FILE):
        os.remove(TEST_DB_FILE)
    yield
    engine.dispose()
    if os.path.exists(TEST_DB_FILE):
        try:
            os.remove(TEST_DB_FILE)
        except PermissionError:
            pass


@pytest.fixture(scope="module")
def session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


async def _test_rate_identifier(request):
    return "test-rate-key"


async def _test_rate_callback(request, response, pexpire):
    return None


class _FakeRedis:
    async def evalsha(self, *args, **kwargs):
        return 0


@pytest.fixture(scope="module", autouse=True)
def disable_rate_limiter():
    original_redis = FastAPILimiter.redis
    original_identifier = getattr(FastAPILimiter, "identifier", None)
    original_callback = getattr(FastAPILimiter, "http_callback", None)
    original_lua_sha = getattr(FastAPILimiter, "lua_sha", None)

    FastAPILimiter.redis = _FakeRedis()
    FastAPILimiter.identifier = _test_rate_identifier
    FastAPILimiter.http_callback = _test_rate_callback
    FastAPILimiter.lua_sha = "test-lua-sha"

    with patch("main.FastAPILimiter.init", new=AsyncMock(return_value=None)):
        try:
            yield
        finally:
            FastAPILimiter.redis = original_redis
            FastAPILimiter.identifier = original_identifier
            FastAPILimiter.http_callback = original_callback
            FastAPILimiter.lua_sha = original_lua_sha


@pytest.fixture(scope="module", autouse=True)
def use_test_session_manager(request):
    if request.module.__name__ != "tests.test_auth":
        yield None
        return

    if not _has_aiosqlite():
        pytest.skip("aiosqlite is required to run auth tests against the test DB")

    test_sessionmanager = DatabaseSessionManager(SQLALCHEMY_ASYNC_DATABASE_URL)
    original_repository_sessionmanager = repository_users.sessionmanager
    repository_users.sessionmanager = test_sessionmanager
    try:
        yield test_sessionmanager
    finally:
        repository_users.sessionmanager = original_repository_sessionmanager
        if test_sessionmanager._engine is not None:
            asyncio.run(test_sessionmanager._engine.dispose())


@pytest.fixture(scope="module")
def client(session):
    def override_get_db():
        yield session

    app.dependency_overrides[get_async_session] = override_get_db
    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()


@pytest.fixture(scope="module")
def user():
    return {"email": "deadpool@example.com", "password": "123456789"}
