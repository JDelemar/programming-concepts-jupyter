#!/bin/bash
# nbconvert-run.sh
# Run all notebooks in this project

CLEAR=""

# parse command-line arguments
while [[ $# -gt 0 ]]
do
    key="$1"

    case $key in
        --clear)
        CLEAR="--clear"
        shift
        ;;
        *)
        # unknown option
        echo "Unknown option: $key"
        exit 1
        ;;
    esac
done

docker run --rm -v $PWD:/opt/app/data --workdir /opt/app/data jdelemar/jupyterlab-dotnet:6.0.202 \
  python ./nbconvert.py $CLEAR
