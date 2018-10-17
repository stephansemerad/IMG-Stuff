
#!/usr/bin/python
## -*- coding: utf-8 -*-

from PIL import Image
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.append(parent)

size = 1000, 1000

def resize(filename):
    im = Image.open(os.path.join(parent+'/assets/img/listings/', filename))
    if not im.mode == 'RGB':
      im = im.convert('RGB')
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(filename,quality=95)
