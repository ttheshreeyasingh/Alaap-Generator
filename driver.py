from sargam_to_western import *
from main import *
from g import *

with open('raga.json', 'r') as f:
    raga_data = json.load(f)

raga = Raga(raga_data)
aalaap = raga.run(Note("S", 1), 2, 16)
indToWest = IndianToWestern()
print(aalaap)


# Open a new file for writing
with open('./frontend/public/aalaap.txt', 'w') as f:
    # Join the items in the list with spaces and write the resulting string to the file
    f.write(" ".join(aalaap))


western_notes = indToWest.sargam_to_western(aalaap, key='C')

g = Grapher()
g.plot(western_notes)
for i in range(len(western_notes)):
    print(western_notes[i], aalaap[i])




