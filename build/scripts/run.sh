#!/bin/bash

function buildAnax () {
  cd /build/
  source envvars.sh
  git clone https://github.com/abrahamrhoffman/AnaxDb.git
  cd AnaxDb
  python setup.py develop
  python setup.py sdist bdist_wheel
  twine upload dist/*
}

function main () {
  buildAnax
}

main
