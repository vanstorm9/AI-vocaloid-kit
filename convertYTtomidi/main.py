from __future__ import unicode_literals
import youtube_dl
import os

import music21
import matplotlib.pyplot as plt
from midiutil.MidiFile import MIDIFile


import sys,os

skipMidiConversion = False

outputJSON = None


def YoutubeToMIDIConvert():

	if not skipMidiConversion:
		# First we convert Youtube video to mp3

		print 'Working with ', sys.argv[1]
		YT_URL = sys.argv[1]

		print os.getcwd()

		'''
		print 'Paste the URL of the Youtube video and press [Enter]'
		YT_URL = raw_input()
		'''
		os.system('rm -r bin')

		os.makedirs('./bin')

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

	####
	print 'File successfully converted!'



YoutubeToMIDIConvert()





