#!/usr/bin/python
## -*- coding: utf-8 -*-
import os.path, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.append(parent)

def check_img(path):
    if img == None or img =='':
        return 'no_img.jpg'
    else:
        if os.path.isfile(path) == True:
            return img
        else:
            return 'no_img.jpg'
