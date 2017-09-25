# Used to form the song input vector that we will used as input for model.py
# We are plotting the structure of the midi file in this script

import music21
import matplotlib.pyplot as plt
import numpy as np
import os

matrix_path = "./songComposer/matrices/input/"
slash = "/"
dash = "-"

#fp = './songComposer/songs/beethoven_movement01.mid'
fp = './songComposer/songs/world-is-mine.mid'
#fp = './songComposer/songs/how-to-world-domination.mid'
#fp = './songComposer/songs/Suteki-Da-Ne.mid'
#fp = './songComposer/songs/Deep-Sea-Girl.mid'

name = "world-is-mine"
#name = "how-to-world-domination"
#name = "suteki-da-ne"
#name = "deep-sea-girl"

def matrixGenerate():
	mf = music21.midi.MidiFile()
	mf.open(fp)
	mf.read()
	mf.close()


	x = []
	y = []

	mainCounter = 0
	prevPitch = 0

	for tracksNum in range (0, len(mf.tracks)):
	    # Prints out the number of events in a track
	    numOfEvents = len(mf.tracks[tracksNum].events)
	    print numOfEvents
	    
	    count = 0
	    for eventInd in range(0,numOfEvents):
		
		# Tracks
		event = mf.tracks[tracksNum].events[eventInd]
		eventType = event.type

		if eventType == 'NOTE_ON':
		    #print track
		    if prevPitch != event.pitch:
			y.append(event.pitch)
			count = count + 1
	      
	    save_path = matrix_path + name + slash 
	    y_set =  name + '-' + str(mainCounter) + '.npy'
	    
	    np.save(save_path + y_set , y)
	 

	    x = []
	    y = []
		    
	    mainCounter = mainCounter + 1
		
	    

