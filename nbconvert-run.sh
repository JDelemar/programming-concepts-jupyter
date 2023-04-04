#!/bin/bash
# nbconvert-run.sh
# Run all notebooks in this project

docker run --rm -v $PWD:/opt/app/data --workdir /opt/app/data jdelemar/jupyterlab-dotnet:6.0.202 \
  jupyter nbconvert --to notebook --inplace --allow-errors --execute --config config.py
