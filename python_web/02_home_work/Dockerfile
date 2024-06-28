# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.10
FROM python:3.12-slim

# Встановимо змінну середовища
# ENV APP_HOME /app

# Встановимо робочу директорію всередині контейнера
# WORKDIR $APP_HOME
WORKDIR .

# COPY poetry.lock $APP_HOME/poetry.lock
# COPY pyproject.toml $APP_HOME/pyproject.toml
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Встановимо залежності всередині контейнера
RUN pip install poetry
#RUN poetry shell
RUN poetry config virtualenvs.create false && poetry install --only main
#RUN pip install -r requirements.txt

# Позначимо порт, де працює застосунок всередині контейнера
EXPOSE 5000

# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["python", "main.py"]