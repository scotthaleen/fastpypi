#!/usr/bin/env bash

set -ex

mypy --show-error-codes fastpypi
black --line-length 119 fastpypi --check
isort --check-only fastpypi
flake8
