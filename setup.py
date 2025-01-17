import sys
from pathlib import Path

from setuptools import setup

assert sys.version_info >= (3, 6), "unimport requires Python 3.6+"

CURRENT_DIR = Path(__file__).parent


def get_long_description():
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()


DESCRIPTION = (
    "A linter, formatter for finding and removing unused import statements."
)
VERSION = "0.9.0"


setup(
    name="unimport",
    version=VERSION,
    description=DESCRIPTION,
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords=["unused", "import"],
    author="Hakan Çelik",
    author_email="hakancelik96@outlook.com",
    url="https://github.com/hakancelik96/unimport",
    project_urls={
        "Documentation": "https://unimport.hakancelik.dev/",
        "Issues": "https://github.com/hakancelik96/unimport/issues",
    },
    license="MIT",
    license_file="LICENSE",
    python_requires=">=3.6",
    packages=["unimport"],
    install_requires=[
        "libcst==0.3.19",
        "pathspec==0.8.1",
        "toml==0.10.2",
        "importlib_metadata==4.5.0",
        "dataclasses==0.6",
        "typing-extensions==3.10.0.0",
    ],
    extras_require={
        "docs": [
            "mkdocs==1.2.1",
            "mkdocs-material==7.1.9",
            "mkdocs-markdownextradata-plugin==0.2.4",
            "mkdocs-minify-plugin==0.4.0",
            "mkdocs-git-revision-date-localized-plugin==0.9.2",
        ],
        "dev": [
            "importlib_metadata==4.5.0",
            "libcst==0.3.19",
            "pathspec==0.8.1",
            "pytest==6.2.4",
            "pytest-cov==2.12.1",
            "semantic-version==2.8.5",
            "toml==0.10.2",
            "dataclasses==0.6",
            "typing-extensions==3.10.0.0",
        ],
    },
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    entry_points={"console_scripts": ["unimport = unimport.__main__:main"]},
)
