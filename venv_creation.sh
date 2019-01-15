#!/usr/bin/env bash

rm -rf venv

virtualenv --no-site-packages  -p /usr/bin/python3 venv
venv/bin/pip3 install --upgrade pip
venv/bin/pip3 install --no-cache-dir -r requirements.txt --process-dependency-links