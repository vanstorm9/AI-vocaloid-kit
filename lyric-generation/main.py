#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import support.sylco as sylco
import support.markovlib as markovlib
import re
import string
#from string import punctuation

txtFilePath = 'text/result.txt'


def num_of_words(words):
        r = re.compile(r'[{}]'.format(punctuation))
        new_words_cont = r.sub(' ',words)
        wordlen = len(new_words_cont.split())
        return wordlen

def splitParagraphIntoSentences(paragraph):
    ''' break a paragraph into sentences
        and return a list '''
    import re
    # to split by multile characters

    #   regular expressions are easiest (and fastest)
    sentenceEnders = re.compile('[.!?,]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList


#print nsyl('multiplication')

#file_ = open('text/combined.txt')
#file_ = open('scraped_data/1a.txt')
#file_ = open('text/lyrics.txt')


print 'Press any key for love song'
typ = raw_input()


file_ = open(txtFilePath)


while True:
        markov = markovlib.Markov(file_)
        text = markov.generate_markov_text()
        sentences = splitParagraphIntoSentences(text)
        for s in sentences:
                #senlen = sylco.sylco(s)
                print s.strip().capitalize()
		print ''

	print ''
        print ''
        
        print 'Press any key for love song'
        typ = raw_input()

       	file_ = open(txtFilePath)

        print ''
        print ''
