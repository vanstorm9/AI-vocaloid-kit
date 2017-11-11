import convertYTtoMidi.converter as ytc
import lyricGeneration.lyricGenerator as lg
import songComposer.matrixGenerate as mg
import songComposer.train as train
import songComposer.generate as gen

import sys
import os

txtPath = './lyricGeneration/text/'
#skipYT = True
skipYT = False

#justTrain = True
justTrain = False

#justGenerate = True
justGenerate = False

checkmark = True
#checkmark = False

#epoch = 1000
epoch = 1

# bin setup

if not justGenerate or not justTrain:
	os.system('rm -r bin')
	os.makedirs('./bin')
	os.makedirs('./bin/model')
	os.makedirs('./bin/output')



if not (skipYT and not justGenerate) and not justTrain:
	url = sys.argv[1]

	print 'Converting Youtube video to MIDI. . .'
	ytc.YoutubeToMIDIConvert(url)


## Use lyric generator
lg.lyricGenerator(txtPath)

if not justGenerate:

	# Use song composer
	print 'Generating numpy matrix of song'
	mg.matrixGenerate()

	print 'Training. . .'
	train.train(epoch, checkmark)

print 'Generating midi file. . .'
gen.generate()


print 'Done'
