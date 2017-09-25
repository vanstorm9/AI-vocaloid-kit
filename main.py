import convertYTtoMidi.converter as ytc
import lyricGeneration.lyricGenerator as lg
import songComposer.matrixGenerate as mg
import songComposer.train as train
import songComposer.generate as gen

import sys

txtPath = './lyricGeneration/text/'
skipYT = True


if not skipYT:
	url = sys.argv[1]

	print 'Converting Youtube video to MIDI. . .'
	ytc.YoutubeToMIDIConvert(url)

## Use lyric generator
lg.lyricGenerator(txtPath)

# Use song composer
mg.matrixGenerate()

train.train()

print 'Done'
