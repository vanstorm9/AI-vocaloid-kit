# Load Larger LSTM network and generate melody from multiple tracks
import sys
import numpy
import matplotlib.pyplot as plt
from midiutil.MidiFile import MIDIFile

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

from time import time

import os.path

# Values to change depending on song
weightnameAr = [
	'../modelToUse/domination-model.h5',
	'../modelToUse/domination-model-1.h5'
	]


root_path = '../matrices/input' 
#name = '/how-to-world-domination/how-to-world-domination-'
#name = '/deep-sea-girl/deep-sea-girl-'
name = '/world-is-mine/world-is-mine-'
end_tag_npy = '.npy'


seq_length = 300
numOfNotesGen = 500


trackCount = 0

MyMIDI = MIDIFile(len(weightnameAr))

prevPath = ''

for weightname in weightnameAr:
	print 'Track ', trackCount

	t0 = time()

	read_path = root_path + name + str(trackCount) + end_tag_npy 

	if not os.path.exists(read_path):
		print 'Path does not exist, using previously working path'
		read_path = prevPath
	else:
		prevPath = read_path

	
	
	raw_text = numpy.load(read_path)


	# Loading raw text
	# create mapping of unique chars to integers, and a reverse mapping
	chars = sorted(list(set(raw_text)))
	char_to_int = dict((c, i) for i, c in enumerate(chars))
	int_to_char = dict((i, c) for i, c in enumerate(chars))

	# summarize the loaded data
	n_chars = len(raw_text)
	n_vocab = len(chars)

	# prepare the dataset of input to output pairs encoded as integers
	dataX = []
	dataY = []
	for i in range(0, n_chars - seq_length):
		seq_in = raw_text[i:i + seq_length]
		seq_out = raw_text[i + seq_length]
		dataX.append([char_to_int[char] for char in seq_in])
		dataY.append(char_to_int[seq_out])
	n_patterns = len(dataX)

	# reshape X to be [samples, time steps, features]
	X = numpy.reshape(dataX, (n_patterns, seq_length, 1))

	# normalize
	X = X / float(n_vocab)

	# one hot encode the output variable
	y = np_utils.to_categorical(dataY)


	# define the LSTM model
	model = Sequential()
	model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
	model.add(Dropout(0.1))
	model.add(LSTM(256))
	model.add(Dropout(0.1))
	model.add(Dense(y.shape[1], activation= 'softmax' ))



	# load the network weights
	# Adding files
	model.load_weights(weightname)
	model.compile(loss= 'categorical_crossentropy' , optimizer= 'adam' )

	# pick a random seed
	start = numpy.random.randint(0, len(dataX)-1)
	pattern = dataX[start]


	xPlot = []
	yPlot = []
	
	# generate notes
	for i in range(numOfNotesGen):
		
		if i%100 == 0:
			print i		

		x = numpy.reshape(pattern, (1, len(pattern), 1))
		x = x / float(n_vocab)
		prediction = model.predict(x, verbose=0)
		index = numpy.argmax(prediction)

		# If we are testing with different song seed, deal with problem of into_to_char sync problem
		if not int_to_char.has_key(index):
			lastVal = int_to_char.keys()[-1]
			index = index - lastVal
		
		result = int_to_char[index]
		seq_in = [int_to_char[value] for value in pattern]
		
		#print result	
		yPlot.append(result)
		xPlot.append(i)
		#sys.stdout.write(result)
		pattern.append(index)
		pattern = pattern[1:len(pattern)]
	

	track = trackCount
	channel = 0
	duration = 6
	volume = 100
	tempo = 180
	
	MyMIDI.addTempo(track,0,tempo)


	for i in range(0,len(xPlot)-1):
		timeStep = xPlot[i]
		pitch = yPlot[i]

		MyMIDI.addNote(track, channel, pitch, timeStep, duration, volume)

	trackCount = trackCount + 1

	print (time() - t0), 's'


# Write the midi file
binfile = open("result.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

print "\nDone."
