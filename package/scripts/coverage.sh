#!/usr/bin/env bash

set -e
set -x

pytest --cov=fastpypi_package --cov-report=term-missing fastpypi_package/tests "${@}"
