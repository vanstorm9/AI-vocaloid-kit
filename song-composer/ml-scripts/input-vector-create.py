# Used to form the song input vector that we will used as input for model.py
# We are plotting the structure of the midi file in this script

import music21
import matplotlib.pyplot as plt
import numpy as np
import os

matrix_path = "../matrices/input/"
slash = "/"
dash = "-"

#fp = '../songs/beethoven_movement01.mid'
fp = '../songs/world-is-mine.mid'
#fp = '../songs/how-to-world-domination.mid'
#fp = '../songs/Suteki-Da-Ne.mid'
#fp = '../songs/Deep-Sea-Girl.mid'

name = "world-is-mine"
#name = "how-to-world-domination"
#name = "suteki-da-ne"
#name = "deep-sea-girl"


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
        
    
print 'Done'

