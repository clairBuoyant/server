FROM python:3.11-slim AS python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# builder-base is used to build dependencies
FROM python-base AS builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -

# We copy our Python requirements here to cache them
# and install only runtime deps using poetry
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./
COPY ./pyproject.toml ./
RUN poetry install --no-dev


# 'development' stage installs all dev deps and can be used to develop code.
# For example using docker-compose to mount local volume under /server
FROM python-base AS development
ENV FASTAPI_ENV=development

# Copying poetry and venv into image
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# Copying in our entrypoint
COPY ./docker/docker-entrypoint /docker-entrypoint
RUN chmod +x /docker-entrypoint

# venv already has runtime deps installed we get a quicker install
WORKDIR $PYSETUP_PATH
RUN poetry install

WORKDIR /backend
COPY ./server /backend/server
COPY ./alembic.ini /backend/
COPY ./migrations /backend/migrations


EXPOSE 8888
ENTRYPOINT /docker-entrypoint $0 $@
CMD ["uvicorn", "--reload", "--host=0.0.0.0", "--port=8888", "server.main:app"]

# 'lint' stage runs black and isort
# running in check mode means build will fail if any linting errors occur
FROM development AS lint
RUN black --config ./pyproject.toml --check server tests
RUN isort --settings-path ./pyproject.toml --recursive --check-only
CMD ["tail", "-f", "/dev/null"]


# 'test' stage runs our unit tests with pytest and
# coverage.  Build will fail if test coverage is under 80%
FROM development AS test
RUN coverage run --rcfile ./pyproject.toml -m pytest ./tests
RUN coverage report --fail-under 80


# 'production' stage uses the clean 'python-base' stage and copies
#  only our runtime deps that were installed in the 'builder-base'
FROM python-base AS production
ENV FASTAPI_ENV=production

COPY --from=builder-base $VENV_PATH $VENV_PATH
COPY ./docker/gunicorn_conf.py /gunicorn_conf.py

COPY ./docker/docker-entrypoint /docker-entrypoint
RUN chmod +x /docker-entrypoint

WORKDIR /backend
COPY ./server /backend/server
COPY ./alembic.ini /backend/
COPY ./migrations /backend/migrations
ENTRYPOINT /docker-entrypoint $0 $@
CMD [ "gunicorn", "-k uvicorn.workers.UvicornWorker", "-c docker/gunicorn_conf.py", "server.main:app"]
