#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy.io import wavfile
import utils
from driver import aalaap
import os


# Dictionary to map Indian classical music notes to piano notes
note_mapping = {
    'S': 'C',
    'r': 'c',
    'R': 'D',
    'g': 'd',
    'G': 'E',
    'm': 'F',
    'M': 'f',
    'P': 'G',
    'd': 'g',
    'D': 'A',
    'n': 'a',
    'N': 'B'
}

# Indian classical music notes
#swaras = ['S', 'R2','G2', 'P', 'D2']

# Map the Indian classical music notes to piano notes
swaras = ['r_2', 'G_2', 'P_2', 'G_2', 'S_2', 'm_2', 'P_2', 'S_2', 'r_2', 'S_2', 'G_2', 'r_2', 'S_2', 'd_1', 'N_1', 'r_2', 'G_2', 'r_2', 'S_2']
piano_notes = [note_mapping[swara[0]] for swara in aalaap]

#print(piano_notes)
for i in range(0,len(piano_notes)):
    if aalaap[i][-1] == '1':
        piano_notes[i] = piano_notes[i] + '4'
    if aalaap[i][-1] == '0':
        piano_notes[i] = piano_notes[i] + '3'
    if aalaap[i][-1] == '2':
        piano_notes[i] = piano_notes[i] + '5'   
    
print(piano_notes)
#right_hand_notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
                    
right_hand_duration = [0.5, 0.5, 0.5, 0.5,
                       0.5, 0.5, 1]*6


factor = [0.68, 0.26, 0.03, 0.  , 0.03]
length = [0.01, 0.6, 0.29, 0.1]
decay = [0.05,0.02,0.005,0.1]
sustain_level = 0.1
right_hand = utils.get_song_data(piano_notes, right_hand_duration, 2,
                                 factor, length, decay, sustain_level)

data = right_hand
data = data * (4096/np.max(data))
#os.mkdir("data")
wavfile.write('data/twinkle_star.wav', 44100, data.astype(np.int16))