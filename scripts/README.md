# Development Scripts

These scripts are provided for development of [clairBuoyant](https://www.github.com/clairBuoyant). The script names are standardized across all repositories for clairBuoyant to simplify the development experience.

## Folder Structure

```
📂 scripts/
├── 📂 db/
│   ├── 📄 create
│   ├── 📄 docker
│   ├── 📄 migrations_autogenerate
│   ├── 📄 migrations_run
│   ├── 📄 seeds
├── 📄 bootstrap
├── 📄 check
├── 📄 clean
├── 📄 coverage
├── 📄 dotenv
├── 📄 init
├── 📄 lint
├── 📄 setup
├── 📄 start
├── 📄 test
└── 📄 uninstall
```

The command to run can be inferred based on the following pattern:

- command: `filename`
  - e.g., `bootstrap`
    - filename: bootstrap
    - subFolderName: n/a
- command: `subFolderName-filename`
  - e.g., `db-migrations_autogenerate`
    - filename: migrations_autogenerate
    - subFolderName: db

## Available Commands

See below for list of available commands.

- `db-create`: create databases locally. [🚧 _currently unsupported_ 🚧]
- `db-docker`: create databases in docker.
- `db-migrations_autogenerate`: autogenerate migration files for db schema changes.

  ```bash
  # recommended: provide revision message between double quotes
  poetry run db-migrations_autogenerate "<optional-descriptive-comment>"

  # without providing revision message
  poetry run db-migrations_autogenerate
  ```

- `db-migrations_run`: apply database schema changes from migration files.
- `db-seeds`: populate database with initial dataset.
- `bootstrap`: resolve all system dependencies the application needs to run.
- `check`: check whether code linting passes.
- `clean`: remove all unnecessary build artifacts.
- `dotenv`: create .env file for development.
- `coverage`: check test coverage.
- `init`: run bootstrap and setup.
- `lint`: run code linting.
- `setup`: install python dependencies and githooks.
- `start`: start server locally with dotenv.
- `test`: run test suite.
- `uninstall`: remove python dependencies and build artifacts.

### Usage

These scripts can be used directly or with `poetry` (**recommended**).

1. Run with poetry: `poetry run <command_name>` (e.g., `poetry run init`) <sup>1</sup>
2. Run directly:
   - `./scripts/<filename>` (e.g., `./scripts/init` or `./scripts/db/docker`)
   - Run `. ./aliases` in your terminal to run any script just by `<command_name>` (e.g., `init` or `db-docker`). <sup>2</sup>

#### Note

1. If you've ran `poetry shell` (i.e., if `which python` outputs "path/to/clairBuoyant/server/.venv/bin/python"), you could just run these scripts by `<command_name>` in terminal (e.g., `init` or `db-docker`).

2. Alternatively, you could run `. ./aliases`. This will load all command names to current shell, so you can call on these scripts by `<command_name>` (e.g., `init` or `db-docker`). This script needs to be re-run every time you start a new terminal session. But, it saves you from prepending `poetry run` every time! :)

### Attribution

Styled after GitHub's ["Scripts to Rule Them All"](https://github.com/github/scripts-to-rule-them-all).
