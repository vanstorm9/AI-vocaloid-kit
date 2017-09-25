from music21 import *
import matplotlib.pyplot as plt
#from midiutil.MidiFile import MIDIFile
import os



#fp = '../songs/beethoven_movement01.mid'
#fp = '../songs/lbtheme.mid'
fp = '../songs/world-is-mine.mid'
#fp = './sample0.mid'
#fp = '../songs/Suteki-Da-Ne.mid'
#fp = '../songs/how-to-world-domination.mid'


mf = midi.MidiFile()
mf.open(fp)
mf.read()
mf.close()



x = []
y = []

for tracksNum in range (0, len(mf.tracks)):
    
    # Prints out the number of events in a track
    numOfEvents = len(mf.tracks[tracksNum].events)
    print numOfEvents
    #print mf.tracks


    # Music21 Initalizatioon
    mtf = midi.MidiFile()
    mt = midi.MidiTrack(1)    
    mtf.tracks = mt


    count = 0

    for eventInd in range(0,numOfEvents):
	#print '------------'
        # Tracks
        track = mf.tracks[tracksNum].events[eventInd]
        trackType = track.type

	
	me = midi.MidiEvent(mt)		
	me.type = trackType
	
	if trackType == 'NOTE_ON':
		me.trackType = trackType
		me.pitch = track.pitch
		me.velocity = track.velocity

		#print '[',me,']'
		#print '[',mt.events,']'
		mt.events[count] = me

		mt.events = me
	if trackType == 'NOTE_OFF':		
		me.trackType = trackType
		me.pitch = track.pitch
		me.velocity = track.velocity
		
		#mt.tracks[0].events[count] = me

	if trackType == 'DeltaTime':

		me.trackType = trackType
		me.pitch = track.pitch
		me.velocity = track.velocity
	if trackType == 'SET_TEMPO':

		me.trackType = trackType
		me.pitch = track.pitch
		me.velocity = track.velocity
	
	#print len(mt.tracks[0].events)
	#print mtf




        count = count + 1
    #print mtf.tracks
    mtf.tracks.append(mt)    

    mtf.open('result.mid')
    mtf.write()
    mtf.close()

    print 'Press enter to continue'
    raw_input()

    '''
    # Setting up new midi file
    MyMIDI = MIDIFile(1)
    track = 0
    time = 0
    channel = 0
    duration = 1
    volume = 100
    tempo = 520


    MyMIDI.addTrackName(track, time, "Sample Track")
    MyMIDI.addTempo(track,time,tempo)
     
    count = 0
    prevPitch = -1

    # Begin reconstruction of the track
    for eventInd in range(0,numOfEvents):
        # Tracks
        track = mf.tracks[tracksNum].events[eventInd]
        trackType = track.type

        if trackType == 'NOTE_ON':
            y.append(track.pitch)
            x.append(count)


            MyMIDI.addNote(track, channel, pitch, time, duration, volume)

	if trackType == 'NOTE_OFF':

            MyMIDI.addNote(track, channel, pitch, time, duration, volume)



        prevPitch = track.pitch

        count = count + 1
    
    # Writing reconstructed track
    binfile = open("result.mid", 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()    
	'''


    '''
    ################################


    for i in range(0,len(x)-1):
        time = x[i]
        pitch = y[i]


    ################################
    '''

            

        
    


