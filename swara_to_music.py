#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy.io import wavfile
import utils
'''
right_hand_notes = ['C4', 'C4', 'G4', 'G4',
                   'A4', 'A4', 'G4',
                   'F4', 'F4', 'E4', 'E4',
                   'D4', 'D4', 'C4',
                   'G4', 'G4', 'F4', 'F4',
                   'E4', 'E4', 'D4',
                   'G4', 'G4', 'F4', 'F4',
                   'E4', 'E4', 'D4',
                   'C4', 'C4', 'G4', 'G4',
                   'A4', 'A4', 'G4',
                   'F4', 'F4', 'E4', 'E4',
                   'D4', 'D4', 'C4']'''

# Dictionary to map Indian classical music notes to piano notes
note_mapping = {
    'S': 'C',
    'R1': 'd',
    'R2': 'D',
    'G1': 'E',
    'G2': 'f',
    'M1': 'F',
    'M2': 'g',
    'P': 'G',
    'D1': 'a',
    'D2': 'A',
    'N1': 'B',
    'N2': 'C'
}

# Indian classical music notes
#swaras = ['S', 'R2','G2', 'P', 'D2']

# Map the Indian classical music notes to piano notes
'''piano_notes = [note_mapping[swara] for swara in swaras]

print(piano_notes)
for i in range(0,len(piano_notes)):
    piano_notes[i] = piano_notes[i] + '4'''

right_hand_notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
                    
right_hand_duration = [0.5, 0.5, 0.5, 0.5,
                       0.5, 0.5, 1]*6


factor = [0.68, 0.26, 0.03, 0.  , 0.03]
length = [0.01, 0.6, 0.29, 0.1]
decay = [0.05,0.02,0.005,0.1]
sustain_level = 0.1
right_hand = utils.get_song_data(right_hand_notes, right_hand_duration, 2,
                                 factor, length, decay, sustain_level)

data = right_hand
data = data * (4096/np.max(data))
wavfile.write('./frontend/public/music.wav', 44100, data.astype(np.int16))