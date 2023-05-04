import random
import json
import math
import numpy as np

from pprint import pprint


with open('raga.json', 'r') as f:
    raga_data = json.load(f)


class Note:
    def __init__(self, swara, octave):
        self.swara = swara
        self.octave = octave

class Raga:

    def __init__(self, data):
        self.motifs = data["motifs"]
        self.swar_vistaar = []
        self.default_octave = 1
        self.all_sargam = [Note("S", 1), Note("r", 1), Note("R", 1), Note("g", 1), Note("G", 1), Note(
            "m", 1), Note("M", 1), Note("P", 1), Note("d", 1), Note("D", 1), Note("n", 1), Note("N", 1)]
        self.forbidden = data["forbidden"]
        self.allowed_notes = self.get_allowed_notes(self.all_sargam)

    def get_allowed_notes(self, sargams):
        allowed_notes = []
        for note in self.all_sargam:
            if note.swara not in self.forbidden:
                allowed_notes.append(note)
        return allowed_notes

    def get_adjacent_notes(self, note, n):
        swara = note.swara
        octave = note.octave

        raga_notes = self.get_allowed_notes(self.all_sargam)
        raga_notes = [note.swara for note in raga_notes]
        num_raga_notes = len(raga_notes)
        # print("raga_notes: ", raga_notes)

        # position of note in raga ascending sequence
        index = raga_notes.index(swara)

        left_adjacent_notes = []
        right_adjacent_notes = []

        for i in range(1, n+1):
            octave = note.octave
            left_index = (index - i) % num_raga_notes
            distance = i
            if (index - i) != left_index:
                octave = octave - 1
            new_note = Note(raga_notes[left_index], octave)
            left_adjacent_notes.append([new_note, distance])
        for i in range(1, n+1):
            octave = note.octave
            right_index = (index + i)
            distance = i

            if (index + i) != (index + i) % int(num_raga_notes):
                octave = octave + 1
            right_index = right_index % num_raga_notes
            new_note = Note(raga_notes[right_index], octave)
            right_adjacent_notes.append([new_note, distance])

        adjacent_notes = left_adjacent_notes + right_adjacent_notes
        return adjacent_notes

    def get_adj_note_prob(self, note, n):


        adjacent_notes = self.get_adjacent_notes(note, n)

        motifs_with_note = []
        for motif in self.motifs:
            if note.swara in motif:
                motifs_with_note.append(motif)

        probs = []
        for adj in adjacent_notes:
            distance = adj[1]
            probability = 1 / (1 + math.exp((distance)))
            probs.append(probability)

        total = sum(probs)
        probs = [prob / total for prob in probs]

        return list(zip(adjacent_notes, probs))
    
    def get_next_note(self, note, n):
        probs = self.get_adj_note_prob(note, n)
        # pick one random note using the probabilities as weights
        next_note = random.choices([prob[0] for prob in probs], weights=[prob[1] for prob in probs], k=1)[0][0]
        return next_note
    
    def get_swar_vistaar(self, note, n, length):
        swar_vistaar = []
        for i in range(length):
            if(len(swar_vistaar) >= length):
                break
            note = self.get_next_note(note, n)
            if random.random() < 0.6:
                motifs_with_note = []
                for motif in self.motifs:
                    if note.swara == motif[0]:
                        motifs_with_note.append(motif)
                
                if len(motifs_with_note) == 0:
                    swar_vistaar.append(note)
                    continue
                else:
                    motif = random.choice(motifs_with_note)

                for swara in motif:
                    swar_vistaar.append(Note(swara, note.octave))
            else:
                swar_vistaar.append(note)
                

        return swar_vistaar
    
    def run(self, note, n, length):
        swar_vistaar = self.get_swar_vistaar(note, n, length)
        output = []
        for swar in swar_vistaar:
            output.append(str(swar.swara + "_" +str(swar.octave)))
        return output


if __name__ == "__main__":
    raga = Raga(raga_data)
    raga.run(Note("S", 1), 2, 16)
