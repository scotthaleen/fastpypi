import sys
import subprocess

from pathlib import Path


def __getattr__(name):
    """
    HACK to make poetry execute shell scripts
    """
    subprocess.run([f"./scripts/{name}.sh"] + sys.argv[1:])
    return lambda: None


def run():
    args = sys.argv[1:]
    p = Path("./scripts")
    options = set(f.stem for f in list(p.glob('*.sh')))

    if next(iter(args), "") not in options:
        print("Invalid script option")
        print("Valid options:")
        print("\t" + "\n\t".join(options))
    else:
        subprocess.run([f"./scripts/{args[0]}.sh"])
