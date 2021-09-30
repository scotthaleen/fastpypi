#!/usr/bin/env bash

set -e
set -x

pytest --cov=fastpypi --cov-report=term-missing fastpypi/tests "${@}"
