import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
# example frequencies

class Grapher():
    
    def __init__(self):
        pass

    def note_to_frequency(self, note):
        """
        Convert a musical note to its frequency in Hz
        """
        n = ord(note[0]) - 59 + (int(note[-1]) * 12)
        f = 2 ** ((n-49)/12) * 440
        return f
    
    def notes_to_frequencies(self, notes):
        freqs = []
        for note in notes:
            freqs.append(self.note_to_frequency(note))
        return freqs
    
    def plot(self, notes):

        freqs = self.notes_to_frequencies(notes)
        x = np.arange(len(freqs))
        
        cs = CubicSpline(x, freqs)

        xfine = np.linspace(0, len(freqs)-1, 1000)
        yfine = cs(xfine)

        plt.plot(yfine, xfine)
        # label each note
        plt.yticks(x)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Notes')
        plt.title('Raga')
        plt.grid(True)
        # 
        # save image
        plt.savefig('plot.png')


# usage
# g = Grapher()
# g.plot(["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"])
