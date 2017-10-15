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

checkmark = True
#checkmark = False

epoch = 1000

# bin setup

os.system('rm -r bin')
os.makedirs('./bin')
os.makedirs('./bin/model')
os.makedirs('./bin/output')



if not skipYT:
	url = sys.argv[1]

	print 'Converting Youtube video to MIDI. . .'
	ytc.YoutubeToMIDIConvert(url)

## Use lyric generator
lg.lyricGenerator(txtPath)

# Use song composer
print 'Generating numpy matrix of song'
mg.matrixGenerate()

print 'Training. . .'
train.train(epoch, checkmark)

print 'Generating midi file. . .'
gen.generate()


print 'Done'
