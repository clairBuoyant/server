# clairBuoyant - Server

## Development

Run all documented commands from the project's **root** folder.

### Requirements

- [Docker >= 20.10](https://docs.docker.com/get-docker)
- [Python >= 3.10](https://www.python.org/downloads/release/python-3105)
- [Poetry >= 1.1.14](https://github.com/python-poetry/poetry)

### Local development with Poetry

1. Create virtualenvs in project's root directory by default:

   - Command to do so: `poetry config virtualenvs.in-project true`)
   - Confirm command was successful: `poetry config --list`

2. Create the virtual environment and install dependencies: `poetry install`

3. Run commands inside the virtual environment: `poetry run <your_command>`

4. Start a development server locally:

   ```
   poetry run uvicorn server.main:app --reload --host localhost --port 8888
   ```

   - API will be available at [localhost:8888](http://localhost:8888/).

   - Swagger docs at [localhost:8888/api/docs](http://localhost:8888/api/docs).

5. Spawn a shell inside the virtual environment with `poetry shell` before running commands like above without needing to invoke `poetry run`.

6. Linting and Testing locally:
   - Execute lint/test in [scripts](/scripts/).

See the [poetry docs](https://python-poetry.org/docs/) for more information.

### Environment Variables

- `DATABASE_URL`: "postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

- `PYTHON_ENV`: "development" or "production" or "test". (default: production)

### Development with Docker

Go to [devBuoyant](https://github.com/clairBuoyant/devBuoyant) for instructions.
