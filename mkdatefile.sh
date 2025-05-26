#!/bin/bash

if [ $# -lt 2 ]; then
  echo "Usage: $0 <folder> <filename>"
  exit 1
fi

TARGET_DIR=$1
FILENAME=$2

DATE=$(date +%Y-%m-%d)
FULL_PATH="${TARGET_DIR}/${DATE}_${FILENAME}"

mkdir -p "$TARGET_DIR"

if [ ! -f "$FULL_PATH" ]; then
  touch "$FULL_PATH"
  echo "Created file: $FULL_PATH"
else
  echo "File already exists: $FULL_PATH"
fi
