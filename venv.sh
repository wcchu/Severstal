#!/usr/bin/env bash
prefix=env
rm -r $prefix
virtualenv --python=/usr/bin/python3 --system-site-packages $prefix
source $prefix/bin/activate
pip install --ignore-installed --no-cache-dir -r requirements.txt
