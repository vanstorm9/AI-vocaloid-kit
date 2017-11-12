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

skipLyrics = False

justGenerate = False

checkmark = False

epoch = 1000

# bin setup


parser = argparse.ArgumentParser()
parser.add_argument("--checkmark", help="save checkmark models for each optimal loss", action='store_true')


parser.add_argument("--skipLyrics", help="Skip parsing the Youtube URL and start training", action='store_true')

parser.add_argument("--justGenerate", help="Skip training and generate music with current model", action='store_true')


#parser.add_argument("--skipYT", help="Skip parsing the Youtube URL and start training", action='store_true')


parser.add_argument("--url", help='Youtube video url to extract video audio from')

args = parser.parse_args()


if args.checkmark:
	print('Checkmark mode on')
	checkmark = True


if args.skipLyrics:
	skipLyrics = True


if args.justGenerate:
	justGenerate = True


# Renew bin folder

if not justGenerate or not skipLyrics:
	os.system('rm -r bin')
	os.makedirs('./bin')
	os.makedirs('./bin/lyric')
	os.makedirs('./bin/model')
	os.makedirs('./bin/output')



# Start getting audio data and training

if args.url:
	print('Converting Youtube video to MIDI. . .')
	url = args.url
	ytc.YoutubeToMIDIConvert(url)
else:
	print('Skip Youtube audio extraction')

## Use lyric generator
if not skipLyrics:
	lg.lyricGenerator(txtPath)
else:
	print('Skipped generating lyrics')



if not justGenerate:
	# Use song composer
	print('Generating numpy matrix of song')
	mg.matrixGenerate()

	print('Training. . .')
	train.train(epoch, checkmark)

print('Generating midi file. . .')
gen.generate()


print 'Done'
