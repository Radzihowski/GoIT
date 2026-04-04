"""
Unit tests for src/services/email.py  — target: >75% coverage
Missing lines: 11-48 (entire send_email function body)
"""
import unittest
from unittest.mock import AsyncMock, MagicMock, mock_open, patch

from src.services.email import send_email


class TestEmailService(unittest.IsolatedAsyncioTestCase):

    async def test_send_email_success(self):
        """Covers lines 11-45 — happy path through send_email."""
        html_template = "<html>{{host}} {{username}} {{token}}</html>"

        with patch("builtins.open", mock_open(read_data=html_template)), \
             patch("src.services.email.auth_service.create_email_token", return_value="test-token"), \
             patch("src.services.email.aiosmtplib.send", new=AsyncMock(return_value=None)):

            await send_email(
                email="user@test.com",
                username="testuser",
                host="http://localhost",
            )

    async def test_send_email_smtp_failure_is_caught(self):
        """Covers lines 47-48 — exception is caught and printed, not re-raised."""
        html_template = "<html>{{host}} {{username}} {{token}}</html>"

        with patch("builtins.open", mock_open(read_data=html_template)), \
             patch("src.services.email.auth_service.create_email_token", return_value="test-token"), \
             patch("src.services.email.aiosmtplib.send", new=AsyncMock(side_effect=Exception("SMTP error"))):

            # should NOT raise — exception is caught internally
            await send_email(
                email="user@test.com",
                username="testuser",
                host="http://localhost",
            )

    async def test_send_email_template_not_found_is_caught(self):
        """Covers lines 47-48 — file open failure is caught, not re-raised."""
        with patch("builtins.open", side_effect=FileNotFoundError("template missing")), \
             patch("src.services.email.auth_service.create_email_token", return_value="tok"):

            await send_email(
                email="user@test.com",
                username="testuser",
                host="http://localhost",
            )


if __name__ == "__main__":
    unittest.main()
