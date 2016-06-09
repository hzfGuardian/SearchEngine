#!/usr/bin/env python
# coding=utf-8

import glob
import os

fo = open("trainer", "w")

for fn in glob.glob('../Reuters/' + os.sep + '*.html'):
        file_object = open(fn)
        all_the_text = file_object.read()
        fo.write(all_the_text)
        file_object.close()

fo.close()

