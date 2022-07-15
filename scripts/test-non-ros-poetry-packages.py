# This will run pytest for any non-ros poetry packages.
# i.e. anywhere it finds a pyproject.toml but no package.xml

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
package_xmls = glob(str(Path.cwd() / f"{PACKAGES_DIRECTORY}/**/package.xml"))
package_xml_dirs = [Path(item).parent for item in package_xmls]
pyproject_tomls = glob(str(Path.cwd() / f"{PACKAGES_DIRECTORY}/**/pyproject.toml"))
pyproject_toml_dirs = [Path(item).parent for item in pyproject_tomls]

# Find the packages which are not ros packages...
non_ros_poetry_packages = []
for dir in pyproject_toml_dirs:
    if (dir not in package_xml_dirs):
        non_ros_poetry_packages.append(dir)

for dir in non_ros_poetry_packages:
    print(bcolors.OKCYAN + f"Running tests for {str(dir)}..." + bcolors.ENDC)
    subprocess.call(f'cd {dir} && python3 -m pytest', shell=True)


