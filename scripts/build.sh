#!/bin/sh

# set -e

# CURRENT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
# BASE_DIR="$(dirname "$CURRENT_DIR")"

# cd $BASE_DIR

# docker build --tag clairbuoyant-server --file docker/Dockerfile .

# Exit in case of error
set -e

# Build and run containers
docker-compose up -d

# Hack to wait for postgres container to be up before running alembic migrations
sleep 5;

# Run migrations
docker-compose run --rm backend alembic upgrade head

# Create initial data
docker-compose run --rm backend python3 server/seed_initial_data.py