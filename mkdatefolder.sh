#!/bin/bash

if [ $# -lt 2 ]; then
  echo "Usage: $0 <parent-folder> <name>"
  exit 1
fi

PARENT_DIR=$1
FOLDER_NAME=$2

DATE=$(date +%Y-%m-%d)
FULL_PATH="${PARENT_DIR}/${DATE}_${FOLDER_NAME}"

if [ ! -d "$FULL_PATH" ]; then
  mkdir -p "$FULL_PATH"
  echo "Created folder: $FULL_PATH"
else
  echo "Folder already exists: $FULL_PATH"
fi
