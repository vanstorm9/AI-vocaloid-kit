import convertYTtomidi.converter as ytc
import lyricGeneration.lyricGenerator as lg

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

print 'Done'

