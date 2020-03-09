from setuptools import setup, find_packages
from os.path import realpath, dirname, join
import re
DISTNAME = "smart_odds"
DESCRIPTION = "analysing tennis data"
AUTHOR = "Priya Shantharam"
PROJECT_ROOT = dirname(realpath(__file__))
REQUIREMENTS_FILE = join(PROJECT_ROOT, "requirements.txt")
with open(REQUIREMENTS_FILE) as f:
    install_reqs = f.read().splitlines()
test_reqs = ["pytest", "pytest-cov"]

if __name__ == "__main__":
    setup(
        name=DISTNAME,
        version="0.1.0-dev0",
        description=DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,
        install_requires=install_reqs,
        tests_requires=test_reqs,
        test_suite="nose.collector",
    )
