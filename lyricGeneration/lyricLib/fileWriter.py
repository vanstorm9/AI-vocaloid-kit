#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from importlib import reload

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

def fileWriter(rootPath):


        tf_str = rootPath + 'romaji.txt'
        result_str = rootPath + 'result.txt'
        t_hira_str = rootPath + 'hiragana.txt'
        sf_str = rootPath + 'jap.txt'


        text_file = open(tf_str, 'w')
        result_file = open(result_str, 'w')
        text_fileHira = open(t_hira_str, 'w')
        sourceFile = open(sf_str)


        with sourceFile as f:
                for line in f:
                        if line.isspace():
                                continue


                        line = line.replace('（','')
                        line = line.replace('）','')
                        line = line.replace(' (','')
                        line = line.replace(') ','')
                        line = line.replace('(','')
                        line = line.replace(')','')

                        result_file.write(line)

                        if only_roman_chars(line):
                                text_file.write(line)
                                text_fileHira.write(line)
                                continue


                        line = kanji_to_romaji(line) + '.\n'
                        lineHira = romkan.to_hiragana(line)

                        text_file.write(line)


                        text_fileHira.write(lineHira)

                        if 'str' in line:
                                break

        text_file.close()
        text_fileHira.close()
        result_file.close()

