import logging
from pathlib import Path
from subprocess import call
from sys import argv
from typing import Callable


def _handle_argv(command_name: str) -> tuple[str, str]:
    requested_script = argv[0].split("-")

    dirname, filename = (
        requested_script if len(requested_script) > 1 else (None, command_name)
    )
    comment_if_migrations_autogenerate = argv[1] if len(argv) > 1 else ""

    return (
        _set_script_path(filename=str(filename), subfolder=str(dirname)),
        comment_if_migrations_autogenerate,
    )


def _set_script_path(filename: str, subfolder: str) -> str:
    scripts_dir = Path(__file__).parent

    scripts_subdirectory = scripts_dir.joinpath(subfolder)
    script_in_scripts_subdirectory = scripts_subdirectory.joinpath(filename)

    return (
        str(script_in_scripts_subdirectory)
        if scripts_subdirectory.exists() and script_in_scripts_subdirectory.exists()
        else str(scripts_dir.joinpath(filename))
    )


def __getattr__(command_name: str) -> Callable[[], None]:
    def execute_script() -> None:
        script, user_arg = _handle_argv(command_name)
        try:
            call([script, user_arg])
        except KeyboardInterrupt:
            logging.info("Ctrl + C")

    return execute_script
