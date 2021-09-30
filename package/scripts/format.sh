#!/bin/sh -e
set -x

# Sort imports one per line, so autoflake can remove unused imports
isort --force-single-line-imports fastpypi_package

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place fastpypi_package --exclude=__init__.py
black --line-length 119 fastpypi_package
isort fastpypi_package
