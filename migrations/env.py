import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool, text
from sqlalchemy.ext.asyncio import AsyncEngine

from server.core.config import get_settings
from server.db.base import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


settings = get_settings()


def include_name(name, type_, _):
    if type_ == "table":
        return name in target_metadata.tables
    else:
        return True


def get_db_url():
    return settings.DATABASE_URL


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=get_db_url(),
        target_metadata=target_metadata,
        include_name=include_name,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(
        connection=connection,
        include_name=include_name,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.execute(text("CREATE EXTENSION IF NOT EXISTS postgis"))
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    """TODO: rework testing approach with 12 Factors in mind.
        if settings.PYTHON_ENV == PythonEnv.TEST:
            # connect to primary db
            default_engine = create_async_engine(get_db_url(), isolation_level="AUTOCOMMIT")
            # drop testing db if it exists and create a fresh one
            async with default_engine.connect() as default_conn:
                await default_conn.execute(text("DROP DATABASE IF EXISTS postgres_test"))
                await default_conn.execute(text("CREATE DATABASE postgres_test"))
    """  # noqa: E501,W505,

    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = settings.DATABASE_URL
    connectable = AsyncEngine(
        engine_from_config(
            configuration,
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
            future=True,
        )
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
