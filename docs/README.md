# clairBuoyant - Server

## Development

Run all [documented commands](../scripts/README.md) from the project's **root** folder.

For example, once all system dependencies are installed you may run:
`poetry run init` to complete the prerequisite setup.

### System Dependencies

Install the following required dependencies before proceeding further. We also recommend installing Docker Desktop to simplify your development experience.

#### Required

- [Python >= 3.10](https://www.python.org/downloads/release/python-3105): primary language for server.
- [Poetry >= 1.1.14](https://github.com/python-poetry/poetry): manage Python dependencies and virtualenv.

#### Recommended

- [Docker >= 20.10](https://docs.docker.com/get-docker): simplify database management for development.

### Getting Started

For your initial setup (or if you've deleted your local database and want to start anew), run `poetry run init` in your terminal to get started like so:

```shell
# executes scripts/bootstrap and scripts/setup.
poetry run init

# start development server locally
poetry run start
```

Alternatively, you may load script aliases to your current shell and execute them without `poetry` like so:

```shell
# add scripts aliases to current shell.
. ./aliases

# executes scripts/bootstrap and scripts/setup.
init

# start development server locally
start
```

#### Working with Poetry

Some of `poetry`'s most frequently used commands are documented below:

1. Create the virtual environment and install dependencies: `poetry install`

2. Run commands inside the virtual environment: `poetry run <your_command>`

3. Start a development server locally: `poetry run start`

   - API will be available at [localhost:8888/api](http://localhost:8888/api).
   - API documentation will be available at [localhost:8888/api/docs](http://localhost:8888/api/docs).

4. Spawn a shell inside the virtual environment with `poetry shell` before running commands like above without needing to invoke `poetry run`.

   - this enables us to access the repository's dependencies and scripts directly like so:

     ```bash
     poetry shell
     start # instead of poetry run start
     ```

5. Linting and Testing locally:
   - Execute [lint](../scripts/lint), [test](../scripts/test) and from [scripts folder](../scripts/README.md).

If you'd like to learn more about `poetry`, check their [documentation](https://python-poetry.org/docs/).

### Environment Variables

For development purposes, please ensure you have the following variables defined in `.env`.

- `DATABASE_URL`: "postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"
- `POSTGRES_DB`: "clairbuoyant" (default: clairbuoyant)
- `POSTGRES_USER`: "postgres" (default: randomly generated value)
- `POSTGRES_PASSWORD`: "postgres" (default: randomly generated value)
- `PYTHON_ENV`: "development" or "production" or "test". (default: production)

### Development with Docker

Go to [devBuoyant](https://github.com/clairBuoyant/devBuoyant) for instructions.
