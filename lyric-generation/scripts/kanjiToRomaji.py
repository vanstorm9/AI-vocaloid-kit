#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from kanji_to_romaji import kanji_to_romaji
import romkan
import string

import unicodedata as ud

latin_letters= {}

def is_latin(uchr):
    try: return latin_letters[uchr]
    except KeyError:
         return latin_letters.setdefault(uchr, 'LATIN' in ud.name(uchr))

def only_roman_chars(unistr):
    return all(is_latin(uchr)
           for uchr in unistr
           if uchr.isalpha())


text_file = open('../text/romaji.txt', 'w')
text_fileHira = open('../text/hiragana.txt', 'w')

with open('../text/jap.txt') as f:
   for line in f:

       if line.isspace():
		continue


       line = line.replace('（','')
       line = line.replace('）','')
       line = line.replace(' (','')
       line = line.replace(') ','')
       line = line.replace('(','')
       line = line.replace(')','')


       if only_roman_chars(line.decode('utf-8')):
		text_file.write(line)
		text_fileHira.write(line)
		continue


       line = kanji_to_romaji(line) + '.\n'
       lineHira = romkan.to_hiragana(line).decode('utf-8')

       text_file.write(line)


       text_fileHira.write(lineHira)

       if 'str' in line:
          break

text_file.close()
text_fileHira.close()

'''
'''
