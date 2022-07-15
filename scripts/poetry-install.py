# This will run poetry install alongside any pyproject.tomls

from glob import glob
from pathlib import Path
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


PACKAGES_DIRECTORY = "packages"
pyproject_tomls = glob(str(Path.cwd() / f"{PACKAGES_DIRECTORY}/**/pyproject.toml"))
pyproject_toml_dirs = [Path(item).parent for item in pyproject_tomls]


for dir in pyproject_toml_dirs:
    print(bcolors.OKCYAN + f"Poetry install {str(dir)}..." + bcolors.ENDC)
    subprocess.call(f'cd {dir} && poetry install', shell=True)

