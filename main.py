import convertYTtomidi.converter as ytc
import sys

url = sys.argv[1]

print 'Converting Youtube video to MIDI. . .'
ytc.YoutubeToMIDIConvert(url)

print 'Done'

