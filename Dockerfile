FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project

COPY . .

RUN uv sync --frozen

EXPOSE 8000

CMD ["uv", "run", "fastapi", "run", "src/devshowcase/app.py", "--host", "0.0.0.0", "--port", "8000"]