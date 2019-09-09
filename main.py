import songComposer.matrixGenerate as mg
import songComposer.train as train
import songComposer.generate as gen

import sys
import os
import argparse

# python main.py --checkmark --url (URL)

txtPath = './lyricGeneration/text/'

#skipLyrics = False
skipLyrics = True

justGenerate = False

checkmark = False

epoch = 1000

# bin setup


parser = argparse.ArgumentParser()
parser.add_argument("--checkmark", help="save checkmark models for each optimal loss", action='store_true')


parser.add_argument("--skipLyrics", help="To skip generation of lyrics", action='store_true')

parser.add_argument("--skipTraining", help="Skip training the neural network", action='store_true')

parser.add_argument("--justGenerate", help="Skip training and generate music with current model", action='store_true')

parser.add_argument("--epoch", help="Number of epochs for training")

parser.add_argument("--url", help='Youtube video url to extract video audio from')
parser.add_argument("--midiInput", help="Feed in input midi file path")

args = parser.parse_args()


if args.epoch:
	epoch = int(args.epoch)

if args.checkmark:
	print('Checkmark mode on')
	checkmark = True


if args.skipLyrics:
	skipLyrics = True
else:

	import lyricGeneration.lyricGenerator as lg

if args.justGenerate:
	justGenerate = True


# Renew bin folder

if not justGenerate or not skipLyrics or not justTraining:
	os.system('rm -r bin')
	os.makedirs('./bin')
	os.makedirs('./bin/lyric')
	os.makedirs('./bin/model')
	os.makedirs('./bin/output')



# Start getting audio data and training

if args.url:
	# The import statement is here in order to make the import optional

	import convertYTtoMidi.converter as ytc
	

	print('Converting Youtube video to MIDI. . .')
	url = args.url
	ytc.YoutubeToMIDIConvert(url)
else:
	print('Retrieving import midi file. . .')
	
	if args.midiInput:
		cpPath = 'cp ' + args.midiInput + ' ./bin/output.mid' 
		os.system(cpPath)
	else:
		print('')
		print('You need to choose a Youtube video link using "--url" or choose an input midi file using "--midiInput"')
		exit()

## Use lyric generator
if not skipLyrics:
	lg.lyricGenerator(txtPath)
else:
	print('Skipped generating lyrics')



if not args.skipTraining:
	# Use song composer
	print('Generating numpy matrix of song')
	mg.matrixGenerate()

	print('Training. . .')
	train.train(epoch, checkmark)

print('Generating midi file. . .')
gen.generate()


print('Done')
