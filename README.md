# **THIS REPOSITORY IS DEPRECIATED**

This is a old version of the AI Vocaloid Kit. The repository of the new version is located here:

https://github.com/vanstorm9/AI-Vocaloid-Kit-V2

# AI-vocaloid-kit
A Python kit that uses deep learning to generate vocaloid music. Developers and musicians can now have AI support to aid and inspire ideas for their next vocaloid song.

Takes in Youtube video URL or midi files and use LSTM neural networks in order to study pattern of a song and generate it’s own unique music (in the form of midi file) as well as Markov Models to generate its own accompanying lyrics.

That midi file and generated lyrics can be then fed into a Vocaloid software (tested on Vocaloid Editor 4) to have the Vocaloid sing your AI generated song.

Thing this kit is capable of:
Retrieving Youtube videos to use as input for LSTM neural network
Use midi files as input for LSTM neural network
Generate lyrics based on single file text file (serves as input data)
Train and generate its own song in the form of midi file (that can be fed into Vocaloid software)




# **Dependencies:**
**General python libraries**
- Scipy: https://www.scipy.org/install.html

**Note:**
This program has been worked on and tested in Python 2.7 and probably works in Python 3 as well.

However, if you are having trouble running on Python 3, it is recommended you try it with Python 2 with commands like these:
```
	python2 [python commands]
	pip2 [package you are trying to install]
```

**Requirements for running Youtube to midi converter**

- Youtube DL:  https://github.com/rg3/youtube-dl

- Music21: http://web.mit.edu/music21/

- midiutil: https://pypi.python.org/pypi/MIDIUtil/

- Melodia (credits to Justin Salamon)  @justinsalamon


Follow all dependencies requirements for installing Melodia here:
https://github.com/justinsalamon/audio_to_midi_melodia


**Requirements for training**
- Keras: https://github.com/fchollet/keras
- Music21: http://web.mit.edu/music21/
- midiutil: https://pypi.python.org/pypi/MIDIUtil/




# **__How to run:__**

**__Running entire process:__**


**Sample query to run:**
```
	python main.py --url https://www.youtube.com/watch?v=KMHXgUr7gYM --checkmark --epochs 500
```
**If the Youtube converter fails to run (probably due to improperly installed dependencies), you can try to run this instead:**
```
	python main.py --checkmark --midiInput ./example/0.mid --checkmark --epochs 500
```

# **__Command explanation:__**

**Using Youtube video as input:**
```
  	python main.py --url [Youtube URL link]
```
**Example:**
```
  	python main.py --url https://www.youtube.com/watch?v=KMHXgUr7gYM 
```

**Using midi file as input**
```
	python main.py --midiInput [midi file path] 
```

**Example:**
```
	python main.py --checkmark --midiInput ./example/0.mid 
```	



# **__Additional commands:__**


**Generate song with a model and song matrix:**
```
	python generate.py --model [input model path] --matrix [input matrix path] --output [output midi path]
```
**Only generate lyrics:**
```
	python createLyrics.py --data [input text file path] --output [output file path]
```

