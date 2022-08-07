from os import path
from pathlib import Path
from subprocess import call
from sys import argv


def path_to_script(name: str) -> str:
    scripts_directory = path.dirname(__file__)
    scripts_path = Path(scripts_directory)

    folder_or_file = argv[0].split("-")

    # TODO: remove comments before merging
    # ff, fn = argv[0].split("-") if len(argv) else [name, None]
    # name if len(argv) > 0 and name != fof[0] else (name, None)

    return (
        str(scripts_path.joinpath(folder_or_file[0]).joinpath(folder_or_file[1]))
        if scripts_path.joinpath(folder_or_file[0]).is_dir()
        else str(scripts_path.joinpath(name))
    )


def __getattr__(name: str):
    def execute_script():
        # TODO: incorporate try/except
        file = path_to_script(name)
        call(file)

    return execute_script
