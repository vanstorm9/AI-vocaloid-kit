# This script is to create midi files playing only one track of a song

from music21 import *
import matplotlib.pyplot as plt
from midiutil.MidiFile import MIDIFile
import os



#fp = '../songs/beethoven_movement01.mid'
#fp = '../songs/lbtheme.mid'
#fp = '../songs/world-is-mine.mid'
#fp = './sample0.mid'
#fp = '../songs/Suteki-Da-Ne.mid'
fp = '../songs/how-to-world-domination.mid'

selectedTrackNum = 1

#printTracks = True
printTracks = False

programChangeOn = False
deltaTimeOn = False


### Music21 Initalizations
mf = midi.MidiFile()
mf.open(fp)
mf.read()
mf.close()
###

### MIDIUtil Initalizations
MyMIDI = MIDIFile(len(mf.tracks))
volume = 100
tempo = 680
duration = 6   # interval time that key is still pressed
###

MyMIDI.addTempo(0,0,tempo)

prevPitch = -1

mtf = midi.MidiFile()



mt = midi.MidiTrack(len(mf.tracks))
#mtf.tracks = mt


# Gets the number of events in our chosen track
numOfEvents = len(mf.tracks[selectedTrackNum].events)
tracksNum = selectedTrackNum

count = 0

# Begin reconstruction of the track
for eventInd in range(0,numOfEvents):

	event = mf.tracks[tracksNum].events[eventInd]
	eventType = event.type

	me = midi.MidiEvent(mt)		
	me.type = eventType


	# event
	event = mf.tracks[tracksNum].events[eventInd]
	eventType = event.type

	if printTracks:
		print event

	pitch = event.pitch
	velocity = event.velocity
	channel = event.channel
	time = event.time
	volume = event.velocity


	if deltaTimeOn:
		# determine the duration using DeltaTime
		# First checking if we are at last note o track
		if numOfEvents > eventInd + 1:

		    # Now we get DeltaTime from the next MidiEvent and use that as duration
		    nextStepType = mf.tracks[tracksNum].events[eventInd + 1]
		    if nextStepType.type == 'DeltaTime':
			duration = nextStepType.time/100		



	if time is not None:
	    time = event.time
	else:
	    time = count



	if eventType == 'NOTE_ON':


	    MyMIDI.addNote(0, channel, pitch, time, duration, volume)

	# Controls instruments	
	if programChangeOn:		
		if eventType == 'PROGRAM_CHANGE':
		    MyMIDI.addProgramChange(0, channel, time, event.data)
	
		
	if eventType == 'CONTROLLER_CHANGE':
	    MyMIDI.addControllerEvent(0, channel, time, event._parameter2, event._parameter1)
	

	prevPitch = event.pitch

	count = count + 1


# Writing reconstructed track
print 'Went through Track ', selectedTrackNum

binfile = open("result.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()    
