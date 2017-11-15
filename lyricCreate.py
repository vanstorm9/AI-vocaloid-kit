import lyricGeneration.lyricGenerator as lg
import argparse
import sys
import os

# python lyricCreate.py --data [path] --output [path] 

parser = argparse.ArgumentParser()

parser.add_argument("--data", help="Path of the text file serving as the dataset input", required=True)

parser.add_argument("--output", help="Path of the output text file containing lyrics", required=True)

args = parser.parse_args()

lg.lyricGeneratorCustom(args.data, args.output)

print('Lyric text file was generated!')
