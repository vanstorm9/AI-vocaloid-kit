#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#import support.sylco as sylco
import lyricGeneration.support.markovlib as markovlib

import re
import string
import lyricGeneration.lyricLib.fileWriter as fw

#from string import punctuation

#txtFilePath = 'result.txt'
#txtFilePath = 'romaji.txt'
txtFilePath = 'hiragana.txt'


binPath = './bin/lyric/lyric.txt'


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


def lyricGeneratorPlay(txtPath):
	print('Press any key for love song')
	typ = raw_input()

	fw.fileWriter(txtPath)

	txtPath = txtPath + txtFilePath
	file_ = open(txtPath)


	while True:
		markov = markovlib.Markov(file_)
		text = markov.generate_markov_text()
		sentences = splitParagraphIntoSentences(text)
		for s in sentences:
			#senlen = sylco.sylco(s)
			print(s.strip().capitalize())
			print('')
		
		print('Press any key for love song')
		typ = raw_input()

		file_ = open(txtPath)

		print('')
		print('')


def lyricGenerator(txtPath):
	fw.fileWriter(txtPath)

	txtPath = txtPath + txtFilePath
	file_ = open(txtPath)


	binFile = open(binPath, 'w')	

	markov = markovlib.Markov(file_)
	text = markov.generate_markov_text()
	sentences = splitParagraphIntoSentences(text)
	for s in sentences:
		resSen =  s.strip().capitalize()
		print(resSen)
		print('')

		binFile.write(resSen + '\n')

	binFile.close()


def lyricGeneratorCustom(txtPath, outPath):	

	file_ = open(txtPath)


	binFile = open(outPath, 'w')	

	markov = markovlib.Markov(file_)
	text = markov.generate_markov_text()
	sentences = splitParagraphIntoSentences(text)
	for s in sentences:
		resSen =  s.strip().capitalize()
		print(resSen)
		print('')

		binFile.write(resSen + '\n')

	binFile.close()
