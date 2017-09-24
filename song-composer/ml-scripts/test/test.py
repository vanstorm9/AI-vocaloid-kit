import numpy as np
#import midi
from midiutil.MidiFile import MIDIFile

xPlot = np.array([1,2,3,4,5,6,7,8,9,10])
yPlot = np.array([10,20,50,20,30,80,40,20, 10, 23])

MyMIDI = MIDIFile(1)
track = 0
time = 0
channel = 0
duration = 1
volume = 100
tempo = 120

MyMIDI.addTrackName(track, time, "Sample Track")
MyMIDI.addTempo(track,time,tempo)

for i in range(0,xPlot.shape[0]-1):
	time = xPlot[i]
	pitch = yPlot[i]

	MyMIDI.addNote(track, channel, pitch, time, duration, volume)

binfile = open("result.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
