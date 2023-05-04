# Define the sargam array
class IndianToWestern:

    def __init__(self):
        self.sargam = ['S', 'r', 'R', 'g', 'G', 'm', 'M','P', 'd', 'D', 'n', 'N']
        self.chromatic_scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def sargam_to_intervals(self, sargam_seq):
        intervals = []
        for i in range(len(sargam_seq)):
            interval = self.sargam.index(sargam_seq[i])
            intervals.append(interval)
        return intervals

    def sargam_to_western(self, sargam_seqq, key='C'):
        sargam_seq = [sargam_seqq[i][0] for i in range(len(sargam_seqq))]
        octaves = [sargam_seqq[i][-1] for i in range(len(sargam_seqq))]
        intervals = self.sargam_to_intervals(sargam_seq)
        key_index = self.chromatic_scale.index(key)
        western_notes = []
        for interval in intervals:
            next_index = (key_index + interval) % 12
            western_notes.append(str(self.chromatic_scale[next_index]))
        for i in range(len(western_notes)):
            western_notes[i] = western_notes[i] + str(octaves[i])
        return western_notes
    

# indToWest = IndianToWestern()
# sargam_to_intervals = indToWest.sargam_to_western(sargam_seq, key='D#')

# # usage
# key = 'C#'
# western_notes = indToWest.sargam_to_western(sargam_seq, key)
# print(western_notes)
