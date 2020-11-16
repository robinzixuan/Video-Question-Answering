#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 18:54:20 2020

@author: robin
"""

import json

file = '/Users/robin/Downloads/video/src/output/lists/actions_present/'

with open(file + 'train_labeled.json') as json_file:
    data = json.load(json_file)


for key, val in data:
    