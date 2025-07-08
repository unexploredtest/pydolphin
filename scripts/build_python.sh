#!/bin/bash

# Check if version argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <version>"
  exit 1
fi

VERSION=$1

wget https://www.python.org/ftp/python/$VERSION/Python-$VERSION.tgz
tar xzf Python-$VERSION.tgz
cd Python-$VERSION
./configure CFLAGS="-fPIC" LDFLAGS="-fPIC" --enable-shared
make altinstall

make -j$(nproc)