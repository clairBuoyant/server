# Development Scripts

These scripts are provided for development of [clairBuoyant](https://www.github.com/clairBuoyant). The script names are standardized across all repositories for clairBuoyant to simplify the development experience.

### Commands

<!-- TODO: add DB commands to list and update descriptions before merging -->

- `bootstrap` - Resolve all system dependencies the application needs to run.
- `check` - Check whether code linting passes.
- `clean` - Remove all unnecessary build artifacts.
- `db` - _TBD_
- `dotenv` - _TBD_
- `coverage` - Check test coverage.
- `init` - Execute bootstrap and setup for initial setup.
- `lint` - Run code linting.
- `setup` - Install python dependencies and githooks.
- `start` - Start server locally.
- `test` - Run test suite.
- `uninstall` - Remove all dependencies and build artifacts.

### Usage

The two recommended ways to interact with these scripts are directly or with poetry in your terminal.

1. Run script directly: `./scripts/<name>` (e.g., `./scripts/init`)
2. Run with poetry: `poetry run <name>` (e.g., `poetry run init`)

**NOTE**: If you've ran `poetry shell` (i.e., if `which python` outputs "path/to/clairBuoyant/server/.venv/bin/python"), you could just run these scripts by `<name>` in terminal (e.g., `init`).

### Attribution

Styled after GitHub's ["Scripts to Rule Them All"](https://github.com/github/scripts-to-rule-them-all).
