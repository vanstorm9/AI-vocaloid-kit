#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from kanji_to_romaji import kanji_to_romaji
import string

text_file = open('../text/romaji.txt', 'w')

with open('../text/jap.txt') as f:
   for line in f:

       line = kanji_to_romaji(line) + '.\n'

       text_file.write(line)

       if 'str' in line:
          break

text_file.close()

'''
'''
