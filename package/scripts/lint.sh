#!/usr/bin/env bash

set -ex

mypy --show-error-codes fastpypi_package
black --line-length 119 fastpypi_package --check
isort --check-only fastpypi_package
flake8
