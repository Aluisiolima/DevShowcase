dev:
	uv run fastapi dev src/devshowcase/app.py

run:
	uv run fastapi run src/devshowcase/app.py

install:
	uv sync

test:
	uv run pytest

format:
	uv run ruff format .

lint:
	uv run ruff check .

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .ruff_cache