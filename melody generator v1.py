# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 19:56:08 2023

@author: ily-cloudy
"""
from midiutil import MIDIFile
import random
from random import randrange
import sys
import time

# root note input 
r_note = input("enter root note (lowercase):")

# sets pitch of to that of the root note
if r_note == "c":
    p = 60
elif r_note == "d":
    p = 62
elif r_note == "e":
    p = 64
elif r_note == "f":
    p = 65
elif r_note == "g":
    p = 67
elif r_note == "a":
    p = 57
elif r_note == "b":
    p = 59
else:
    print("invalid root note input, #/b are not yet supported. exiting.")
    time.sleep(3)
    sys.exit(1)

# quality input
quality = input("enter quality (major/minor):")

# creates scale based on chosen quality
if quality == "major":
    scale = [p-12, p-10, p-8, p-7, p-5, p-3, p-1, p, p+2, p+4, p+5, p+7, p+9, p+11, p+12]
elif quality == "minor":
    scale = [p-12, p-10, p-9, p-7, p-5, p-4, p-2, p, p+2, p+3, p+5, p+7, p+8, p+10, p+12]
else:
    print("invalid quality input, only major/minor are supported atm. exiting.")
    time.sleep(3)
    sys.exit(1)

# bpm input
tempo = int(input("enter tempo (bpm):"))

# velocity input
velocity = int(input("enter max velocity (0-100):"))
dv = int(input("enter max velocity difference (< max velocity):"))
if velocity < 0 or velocity > 100:
    print("invalid velocity input. exiting.")
    time.sleep(3)
    sys.exit(1)

# various rythms (a/b implies that they work together)
r_1a = [0, 1.5, 4, 4.5, 5.5, 8, 9.5, 11.5, 12, 13.5]
r_1b = [0, 0.5, 1.5, 4, 4.5, 5.5, 8, 9.5, 11.5, 12, 12.5, 13.5]

r = [r_1a,r_1b]

# set variables
rythm = random.choice(r)
duration = 1

# setting up midi file 
midi = MIDIFile(1)
track = 0
time = 0
midi.addTrackName(track, time, "rng melody")
midi.addTempo(track, time, tempo)
 
for i in rythm:
    midi.addNote(track, 0, random.choice(scale), i, duration, velocity-randrange(dv))

# writes file
with open("melody.mid", "wb") as output_file:
    midi.writeFile(output_file)