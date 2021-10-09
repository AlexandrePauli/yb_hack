import os
from itertools import compress

path = 'data/thommen/Bilder'
# Retrieve name of images
f = os.listdir(path)
f = sorted(f)
id = [x.split('_')[1] for x in f]

id2 = [id[i]!=id[i+1] for i in range(len(id)-1)]
id2.append(True)

toDel = list(compress(f, id2))
print(len(toDel))
##
os.chdir(path)
for name in toDel:
    print(name)
    os.remove(name)





