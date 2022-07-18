# This will run pytest for any non-ros poetry packages.
# i.e. anywhere it finds a pyproject.toml but no package.xml

import subprocess
from glob import glob
from pathlib import Path

from bcolors import bcolors

PACKAGES_DIRECTORY = "packages"
package_xmls = glob(str(Path.cwd() / f"{PACKAGES_DIRECTORY}/**/package.xml"))
package_xml_dirs = [Path(item).parent for item in package_xmls]
pyproject_tomls = glob(str(Path.cwd() / f"{PACKAGES_DIRECTORY}/**/pyproject.toml"))
pyproject_toml_dirs = [Path(item).parent for item in pyproject_tomls]

if __name__ == "__main__":
    print(bcolors.OKBLUE + "Testing non-ros poetry packages..." + bcolors.ENDC)
    # Find the packages which are not ros packages...
    non_ros_poetry_packages = []
    for dir in pyproject_toml_dirs:
        if dir not in package_xml_dirs:
            non_ros_poetry_packages.append(dir)

    for dir in non_ros_poetry_packages:
        print(bcolors.OKCYAN + f"Running tests for {str(dir)}..." + bcolors.ENDC)
        error = subprocess.call(f"cd {dir} && python3 -m pytest .", shell=True)
        if (error):
            raise Exception("Pytest failed")

    print(bcolors.OKGREEN + "Complete" + bcolors.ENDC)
