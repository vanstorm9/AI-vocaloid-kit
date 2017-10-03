# To train the model

import numpy 
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

# load ascii text and convert to lowercase
seq_length = 200
#epoch = 500
epoch = 1000
#read_path = './songComposer/matrices/input/deep-sea-girl/deep-sea-girl-0.npy' 
read_path = './songComposer/matrices/input/output/output-0.npy' 



def train():

	
	raw_text = numpy.load(read_path)


	# create mapping of unique chars to integers, and a reverse mapping
	chars = sorted(list(set(raw_text)))
	char_to_int = dict((c,i) for i,c in enumerate(chars))

	n_chars = len(raw_text)
	n_vocab = len(chars)


	# prepare the dataset of input to output pairs encoded as integers
	dataX = []
	dataY = []

	# dataX is the encoding version of the sequence
	# dataY is an encoded version of the next prediction
	for i in range(0, n_chars - seq_length, 1):
		seq_in = raw_text[i:i + seq_length]
		seq_out = raw_text[i+seq_length]
		dataX.append([char_to_int[char] for char in seq_in])
		dataY.append(char_to_int[seq_out])

		
	n_patterns = len(dataX)
	print "Total Patterns: ", n_patterns

	# reshape X to be [samples, time steps, features]
	X = numpy.reshape(dataX, (n_patterns, seq_length,1))

	# normalize
	X = X/float(n_vocab)

	# one hot encode the output variable
	y = np_utils.to_categorical(dataY)

	print 'X: ', X.shape
	print 'Y: ', y.shape


	# define the LSTM model
	model = Sequential()
	model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
	model.add(Dropout(0.05))
	model.add(LSTM(256))
	model.add(Dropout(0.05))
	model.add(Dense(y.shape[1], activation='softmax'))
	model.compile(loss='categorical_crossentropy', optimizer='adam')


	model.fit(X,y, nb_epoch=epoch, batch_size=64)


	savePath = './bin/model/model.h5'
	
	model.save_weights(savePath)
	print 'Model saved!'
