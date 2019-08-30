# To train the model

import numpy 
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
import os
import glob

# load ascii text and convert to lowercase
seq_length = 200
#epoch = 500
#read_path = './songComposer/matrices/input/deep-sea-girl/deep-sea-girl-0.npy' 
read_path = './songComposer/matrices/input/output/output-0.npy' 



def train(epochNum, checkmark):
	global seq_length
	
	raw_text = numpy.load(read_path)


	# create mapping of unique chars to integers, and a reverse mapping
	chars = sorted(list(set(raw_text)))
	char_to_int = dict((c,i) for i,c in enumerate(chars))

	n_chars = len(raw_text)
	n_vocab = len(chars)

	# prepare the dataset of input to output pairs encoded as integers
	dataX = []
	dataY = []


	seqNum = 0

	if seq_length > n_chars:
		seqNum = n_chars - (n_chars/2)
		seq_length = n_chars/2 
	else:
		seqNum = n_chars - seq_length		
		

	# dataX is the encoding version of the sequence
	# dataY is an encoded version of the next prediction
	#for i in range(0, seqNum, 1):
	for i in range(0, int(seqNum)):
		seq_in = raw_text[i:i + seq_length]

		seq_out = raw_text[i+seq_length]
		dataX.append([char_to_int[char] for char in seq_in])
		dataY.append(char_to_int[seq_out])

		
	n_patterns = len(dataX)
	print("Total Patterns: ", n_patterns)

	if n_patterns <= 0:
		print('')
		print('ERROR: Failed to extract midi notes from this song. Please choose another song to extract from')
		exit()

	# reshape X to be [samples, time steps, features]
	X = numpy.reshape(dataX, (n_patterns, seq_length,1))

	# normalize
	X = X/float(n_vocab)

	# one hot encode the output variable
	y = np_utils.to_categorical(dataY)

	print('X: ', X.shape)
	print('Y: ', y.shape)


	# define the LSTM model
	model = Sequential()
	model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
	model.add(LSTM(256, return_sequences=True))
	model.add(LSTM(256, return_sequences=True))
	model.add(LSTM(256, return_sequences=True))
	model.add(LSTM(256, return_sequences=True))
	model.add(LSTM(256))
	model.add(Dropout(0.1))
	model.add(Dense(y.shape[1], activation='softmax'))



	if checkmark:
		print('Using checkpoint system')


		os.system("rm -r ./songComposer/checkpoints")
		os.system("mkdir ./songComposer/checkpoints")

		model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
		filepath = "./songComposer/checkpoints/weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
		checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
		callbacks_list = [checkpoint]
		
		model.fit(X,y, epochs=epochNum, batch_size=10, callbacks=callbacks_list, verbose=1)

		pathList = []

		folderPath = './songComposer/checkpoints/'
		for a_file in sorted(os.listdir(folderPath)):		
			pathList.append(a_file)

		indexNum = len(pathList) - 1
		path = pathList[indexNum]

		savePath = './bin/model/model.h5'

		cp_cmd = 'cp ' + folderPath + path +' ' +savePath
		print(cp_cmd)
		os.system(cp_cmd)

		print('Model checkmark saved!')


	else:	
		print('Using normal system')
		model.compile(loss='categorical_crossentropy', optimizer='adam')

		model.fit(X,y, epochs=epochNum, batch_size=64)


		savePath = './bin/model/model.h5'
		
		model.save_weights(savePath)
		print('Model saved!')
