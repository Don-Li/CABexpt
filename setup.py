# setup

from setuptools import setup

setup(
    name = "CABexpt",
    version = "0.1",
    descrption = "Package for running operant experiments on the Raspberry Pi.",
    url = "https://github.com/Don-Li/CABexpt",
    license = "GPL 3",
    packages = ["CABexpt"],
    install_requires = [
        'time',
        'pigpio',
        'sys',
        'numpy',
        'os'
        ],
    dependency_links = "https://github.com/Don-Li/CABexpt"
    )