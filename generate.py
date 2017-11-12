import songComposer.generate as gen 
import argparse
import sys
import os

# python generate.py --modelPath [path] --outputFile [path] 

parser = argparse.ArgumentParser()
parser.add_argument("--model", help="Path of the model", required=True)

parser.add_argument("--matrix", help="Path of the numpy matrix of the song", required=True)

parser.add_argument("--output", help="Path of the output midi file", required=True)

args = parser.parse_args()

gen.generateCustomPath(args.model, args.output, args.matrix)

print 'Midi file was generated!'
