#!/bin/bash
set -e

export PATH="$HOME/.local/bin:$PATH"

# Instala apenas as deps de produção
poetry install --without dev

# Executa com Gunicorn
exec poetry run gunicorn "src.main:app" \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 4 \
    --threads 2 \
    --timeout 120
