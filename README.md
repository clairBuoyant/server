# clairBuoyant - Server

## Development

Run all documented commands from the project's **root** folder.

### Requirements

- [Docker >= 20.10](https://docs.docker.com/get-docker)
- [Python >= 3.9](https://www.python.org/downloads/release/python-3101)
- [Poetry >= 1.0](https://github.com/python-poetry/poetry)

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

   - Swagger docs at [localhost:8888/api/v1/docs](http://localhost:8888/api/v1/docs).

5. Spawn a shell inside the virtual environment with `poetry shell` before running commands like above without needing to invoke `poetry run`.

6. Linting and Testing locally:
   - Execute lint/test in [scripts](/scripts/).

See the [poetry docs](https://python-poetry.org/docs/) for more information.

### Development with Docker

1. Build containers for development and seed initial data:

   ```bash
   ./scripts/build.sh
   ```

2. Once you've built your containers, run this command to manage your development environment with hot reloading:

   ```bash
   docker-compose up -d
   ```

   - API will be available at [localhost:8000/api](http://localhost:8000/api/).

   - Swagger docs at [localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs).

#### Additional Commands

You can stop the build at specific stages with the `--target` option:

```bash
docker build --name clairbuoyant-server --file Dockerfile . --target <stage>
```

For example, we can stop at the test stage like so:

```bash
docker build --tag clairbuoyant-server --file docker/Dockerfile --target test .
```

**NOTE**: if target is not specified, docker will build with the 'production' image since it was the last image defined.

We could then get a shell inside the container with:

```bash
docker run -it clairbuoyant-server:latest bash
```
