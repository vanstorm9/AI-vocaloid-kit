import convertYTtoMidi.converter as ytc
import lyricGeneration.lyricGenerator as lg
import songComposer.matrixGenerate as mg
import songComposer.train as train
import songComposer.generate as gen

import sys
import os
import argparse

# python main.py --checkmark --url (URL)

txtPath = './lyricGeneration/text/'
#skipYT = True
skipYT = False

justTrain = False

justGenerate = False

checkmark = False

epoch = 1000

# bin setup

if not justGenerate or not justTrain:
	os.system('rm -r bin')
	os.makedirs('./bin')
	os.makedirs('./bin/lyric')
	os.makedirs('./bin/model')
	os.makedirs('./bin/output')


parser = argparse.ArgumentParser()
parser.add_argument("--checkmark", help="save checkmark models for each optimal loss", action='store_true')

parser.add_argument("--justTrain", help="Skip parsing the Youtube URL and start training", action='store_true')

parser.add_argument("--justGenerate", help="Skip training and generate music with current model", action='store_true')

parser.add_argument("-u", "--url", required=True, help='Youtube video url to extract video audio from')

args = parser.parse_args()


url = args.url

if args.checkmark:
	print('Checkmark mode on')
	checkmark = True

if args.justTrain:
	justTrain = True


if args.justGenerate:
	justGenerate = True

if not (skipYT and not justGenerate) and not justTrain:
	
	print('Converting Youtube video to MIDI. . .')
	ytc.YoutubeToMIDIConvert(url)


## Use lyric generator
lg.lyricGenerator(txtPath)

if not justGenerate:

	# Use song composer
	print('Generating numpy matrix of song')
	mg.matrixGenerate()

	print('Training. . .')
	train.train(epoch, checkmark)

print('Generating midi file. . .')
gen.generate()


print 'Done'
