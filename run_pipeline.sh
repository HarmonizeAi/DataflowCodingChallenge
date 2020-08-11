#!/bin/bash -eu

RUNNER=DirectRunner
TEXT="./in/shakespeare_kinglear.txt"
JOB_NAME="beam-challenge"

# Remove Root directory before running dataflow job.
# gsutil rm -r $ROOT_DIR

# Command to invoke dataflow job.
python pipeline.py \
  --text=${TEXT} \
  --runner=$RUNNER \
  --setup_file=./setup.py \
  --job_name=$JOB_NAME