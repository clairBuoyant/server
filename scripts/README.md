# Development Scripts

These scripts are provided for development of [clairBuoyant](https://www.github.com/clairBuoyant). The script names are standardized across all repositories for clairBuoyant to simplify the development experience.

### Commands

- `bootstrap` - Prepare local development environment.
- `check` - Check whether code linting passes.
- `clean` - Delete any build artifacts.
- `coverage` - Check test coverage.
- `init` - Execute bootstrap and setup for initial setup.
- `lint` - Run code linting.
- `setup` - Initial setup for development dependencies.
- `start` - Start server locally.
- `test` - Run test suite.
- `uninstall` - Delete all dependencies and build artifacts.

### Usage

The two recommended ways to interact with these scripts are directly or with poetry in your terminal.

1. Run script directly: `./scripts/<name>` (e.g., `./scripts/init`)
2. Run with poetry: `poetry run <name>` (e.g., `poetry run init`)

**NOTE**: If you've ran `poetry shell` (i.e., if `which python` outputs "path/to/clairBuoyant/server/.venv/bin/python"), you could just run these scripts by `<name>` in terminal (e.g., `init`).

### Attribution

Styled after GitHub's ["Scripts to Rule Them All"](https://github.com/github/scripts-to-rule-them-all).
