from shutil import get_terminal_size
from subprocess import run
from typing import List


def capture(command: List[str]) -> str:
    return run(command, capture_output=True, text=True, shell=True)


def centered(text: str) -> dict:
    free = (get_terminal_size().columns - len(text)) // 2
    space = free * " "
    return {
        "free": free,
        "length": len(text),
        "space": space,
        "text": f"{space}{text}"
    }


def fill(text: str, sep: str = '-') -> str:
    free = get_terminal_size().columns - len(text)
    space = free * sep
    return f"{text}{space}"


def list_extensions() -> list:
    code_extensions = capture(['code', '--list-extensions']).stdout
    return code_extensions.strip().split('\n')


def parseout(stdout: str) -> str:
    lines = stdout.strip().split('\n')
    return lines[-1].split(' ')[-2]
