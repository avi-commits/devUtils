#!/bin/bash

echo "Installing JDK..."

# Check if brew is installed
if ! [ -x "$(command -v brew)" ]; then
    echo "Error: brew is not installed. Please install brew and run this script again."
    exit 1
fi

# Install JDK
brew install openjdk

echo "JDK installation complete."
