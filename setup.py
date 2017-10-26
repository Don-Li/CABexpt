# setup

from setuptools import setup

setup(
    name = "CABexpt",
    version = "0.1",
    description = "Package for running operant experiments on the Raspberry Pi.",
    url = "https://github.com/Don-Li/CABexpt",
    license = "GPL 3",
    packages = ["CABexpt"],
    author = "Don Li, Stephanie Gomes-Ng",
    author_email = "yli877@aucklanduni.ac.nz, sng089@aucklanduni.ac.nz",    
    install_requires = [
        "pigpio",
        "numpy",
        ],
    dependency_links = ["https://github.com/Don-Li/CABexpt"]
    )