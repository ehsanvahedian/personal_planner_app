#!/bin/bash
cd /app/Backend

uv sync

if [ -f "alembic.ini" ]; then
    echo "Running migrations..."
    uv run alembic upgrade head
else
    echo "alembic.ini not found, skipping migrations"
fi

echo "Starting application..."
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload