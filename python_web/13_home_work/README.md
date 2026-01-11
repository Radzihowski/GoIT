Activation log
=================================
uv sync # To create virtual environments and manage dependencies
uv add fastapi  # Add a package to the virtual environment
uv pip freeze  # List installed packages
uv add fastapi-mail # Add another package
uv pip freeze > requirements.txt # Save installed packages to requirements.txt
docker compose down; docker compose up --build