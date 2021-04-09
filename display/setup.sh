#!/bin/bash

sudo apt-get update
sudo apt-get install python3-pip
python3 -m pip install --user pipenv
pipenv install
pipenv shell