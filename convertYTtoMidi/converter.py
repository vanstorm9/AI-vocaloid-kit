from __future__ import unicode_literals
import youtube_dl
import os

from music21 import *
import matplotlib.pyplot as plt
from midiutil.MidiFile import MIDIFile

import sys,os


outputJSON = None


def YoutubeToMIDIConvert(url):

	# First we convert Youtube video to mp3

	print 'Working with ', url
	YT_URL = url

	print os.getcwd()

	'''
	print 'Paste the URL of the Youtube video and press [Enter]'
	YT_URL = raw_input()
	'''

	ydl_opts = {
	    'outtmpl': 'bin/output.mp3',
	    'format': 'bestaudio/best',
	    'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	    }],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([YT_URL])


	# Then we convert mp3 video to midi
	os.system('python2 ' + os.path.dirname(os.path.realpath(__file__)) + '/support/audio_to_midi_melodia.py bin/output.mp3 bin/output.mid 60 --smooth 0.25 --minduration 0.1 --jams')

	# Insert code here to remove delta time

	selectedTrackNum = 0

	fp = 'bin/output.mid'
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

	binfile = open(fp, 'wb')
	MyMIDI.writeFile(binfile)
	binfile.close()  


	#########
	os.system('cp bin/output.mid convertYTtoMidi/bin/output.mid')

	

	####
	print 'File successfully converted!'






