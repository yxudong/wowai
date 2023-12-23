#!/usr/bin/env bash

gunicorn -D -c gunicorn_conf.py main:app
