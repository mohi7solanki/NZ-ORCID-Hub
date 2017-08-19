#!/usr/bin/env bash

# Script location directory:
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export FLASK_APP=$DIR/main.py
export PYTHONPATH=$(dirname $FLASK_APP)
export LANG=en_US.UTF-8

flask process