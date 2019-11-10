#!/usr/bin/env python3

from setuptools import setup, find_packages
from FindM3H import __version__
import os

try:
    long_description = open("README.md", "rt").read()
except Exception as e:
    long_description = "Find usernames in social networks."


def read_requirements():
    """Parse requirements from requirements.txt.
    """
    
    requirements_path = os.path.join(".", "requirements.txt")
    with open(requirements_path, "r") as f:
        requirements = [line.rstrip() for line in f]
    return requirements


setup(
    name="FindM3H",
    version=__version__,
    description="Find usernames in social networks.",
    long_description=long_description,
    author="Anonhack990"
    packages=find_packages(),
    scripts=["bin/FindM3H"],
    license="MIT",
    install_requires=read_requirements(),
    package_data={"FindM3H": ["web_accounts_list.json"]},
    classifiers=[
        "Programming Language :: Python3",
        "License :: MIT",
        "Environment :: Console",
    ],
)

