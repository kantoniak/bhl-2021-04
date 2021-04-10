#!/bin/bash

# Run commands by hand
sudo apt-get update
sudo apt-get install python3-pip
sudo -H pip3 install -U pipenv

echo "PATH=\$PATH:/usr/local/bin" >> ~/.bashrc
source ~/.bashrc

pipenv install
pipenv shell