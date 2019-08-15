from music21 import *
import matplotlib.pyplot as plt
from midiutil.MidiFile import MIDIFile
import os
import numpy as np


# We load the matrix
matPath = '../matrices/input/output/output-0.npy'


#printTracks = True
printTracks = False


mat_data = np.load(matPath)

if mat_data.ndim == 1:
    mat_data = np.expand_dims(mat_data, axis=0)

### MIDIUtil Initalizations
MyMIDI = MIDIFile(len(mat_data), file_format=1)
volume = 100
tempo = 300
duration = 6   # interval time that key is still pressed
###



prevPitch = -1

mtf = midi.MidiFile()


print(len(mat_data))
mt = midi.MidiTrack(len(mat_data))
#mtf.tracks = mt


for tracksNum,trackPitchAr in enumerate(mat_data):
        print('Track ', tracksNum)

        f = open("notes/notes"+str(tracksNum)+".txt", "w")    
  


        count = 0
        time = count

        #MyMIDI.addTempo(tracksNum,time,tempo)
        MyMIDI.addTempo(tracksNum,0,tempo)
        MyMIDI.addTrackName(tracksNum, 0, 'track'+str(tracksNum))

        duration = 6
        # Begin reconstruction of the track
        for time,pitch in enumerate(trackPitchAr):

            channel = 0

            volume = 100        

            MyMIDI.addNote(track=tracksNum, channel=channel, pitch=pitch, time=time, duration=duration, volume=volume)


# Writing reconstructed track
print('Went through ', str(tracksNum+1), ' tracks')

binfile = open("resultFromMat.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()    
