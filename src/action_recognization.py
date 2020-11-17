#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 18:54:20 2020

@author: robin
"""

import json
import os

file = '/Users/robin/Downloads/video/src/output/lists/actions_present/'

with open(file + 'train_labeled.json') as json_file:
    datas = json.load(json_file)



result = dict()
for key in datas:
    data = dict()
    val = datas[key]
    move = 0
    rotate = 0
    contains = []
    movement = []
    for i in val:
        if i[1] == ['before']:
            if i[0][1][1] != '_rotate':
                move += 1
            else:
                rotate += 1
            if (len(movement) >0 and movement[-1] != i[0][0]) and (len(movement) >1 and movement[-2] != i[0][0]):
                if i[0][0][1] != '_rotate':
                    move += 1
                else:
                    rotate += 1
                movement.append(i[0][0])
            movement.append(i[0][1])    
        if i[1] == ['during']:
            if (len(movement) >0 and movement[-1] != i[0][0]) and (len(movement) >1 and movement[-2] != i[0][0]):
                movement.append(i[0][0])
                if i[0][0][1] != '_rotate':
                    move += 1
                else:
                    rotate += 1
            if (len(movement) >0 and movement[-1] != i[0][1]) and (len(movement) >1 and movement[-2] != i[0][1]) and (len(movement) >2 and movement[-3] != i[0][1]):
                movement.append(i[0][1])  
                if i[0][1][1] != '_rotate':
                    move += 1
                else:
                    rotate += 1
        elif i[1] == ['after']:
            if i[0][0][1] != '_rotate':
                move += 1
            else:
                    rotate += 1
            if (len(movement) >0 and movement[-1] != i[0][1]) and(len(movement) >1 and movement[-2] != i[0][1]):
                if i[0][1][1] != '_rotate':
                    move += 1
                else:
                    rotate += 1
                movement.append(i[0][1])
            movement.append(i[0][0])
    data['rotate_no'] = rotate
    data['item_move'] = movement
    data['item_move_no'] = move
    result[key] = data
    


    