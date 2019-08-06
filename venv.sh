#!/usr/bin/env bash
prefix=~/env-severstal
rm -r $prefix
virtualenv --python=/usr/bin/python3 --system-site-packages $prefix
source $prefix/bin/activate
pip3 install -r requirements.txt
