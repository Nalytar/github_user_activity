#!/bin/bash

# Check if python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python could not be found. Please install Python."
    exit
fi

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found. Please install pip."
    exit
fi

# Install requirements
pip install --ignore-installed -r ./requirements.txt

# Get current script path
SCRIPT_PATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# Add alias to bashrc
echo "alias github-activity='python3 $SCRIPT_PATH/github_activity.py'" >> ~/.bashrc

# Load new alias
source ~/.bashrc