from setuptools import setup, find_packages  # type: ignore
from ollama_shell import __version__, __program__

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]


setup(
    name=__program__,
    version=__version__,
    description="A ollama CLI program to produce shell commands",
    url="https://github.com/diversen/ollama-shell",
    author="Dennis Iversen",
    author_email="dennis.iversen@gmail.com",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    install_requires=REQUIREMENTS,
    entry_points={
        "console_scripts": [
            "ollama-shell = ollama_shell.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.10",
    ],
)