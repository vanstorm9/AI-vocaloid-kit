# AI-vocaloid-kit

A Python kit that uses an AI to generate vocaloid music. Developers and musicians can now have AI support to aid and inspire ideas for their next vocaloid song.

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

