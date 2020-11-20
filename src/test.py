#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 00:32:52 2020

@author: robin
"""
from wordRecognization import word_recogization
encoder = 'what is type of cat'

wr = word_recogization(encoder)
wr.forward()


print(wr.decoder)