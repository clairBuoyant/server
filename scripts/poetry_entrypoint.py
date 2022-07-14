from os import path
from subprocess import call


def __getattr__(name: str):
    def execute_script():
        # TODO: incorporate try/except
        dirname = path.dirname(__file__)
        filename = path.join(dirname, name)
        call(filename)

    return execute_script
