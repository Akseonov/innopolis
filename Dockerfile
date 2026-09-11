# Образ окружения проекта.
# Зависимости берутся ровно из pyproject.toml — того же файла,
# которым ставится локальный .venv для IDEA.
FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_ROOT_USER_ACTION=ignore \
    PYTHONPATH=/app/src

WORKDIR /app

# Отдельным слоем — только метаданные проекта.
# Слой пересобирается лишь при изменении pyproject.toml,
# поэтому правки кода не приводят к переустановке зависимостей.
COPY pyproject.toml README.md ./
RUN mkdir -p src && pip install --no-cache-dir .

# Код не копируется намеренно: он монтируется томом (см. docker-compose.yml),
# так что правки на хосте сразу видны в контейнере.
CMD ["python", "src/init.py"]
