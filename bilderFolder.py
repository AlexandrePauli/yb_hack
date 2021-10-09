import pandas as pd
import os
import numpy as np
import shutil

files = os.listdir('data/thommen/Bilder')
files = sorted(files)
id = [x.split('_')[1] for x in files]
sorten = [x.split('_')[2] for x in files]

for names in sorten:
    if isinstance(names, str):
        if os.path.isdir('data/Images/'+names):
            continue
        else:
            os.mkdir('data/Images/'+names)


path1 = 'data/thommen/Bilder/'
path2 = 'data/Images/'
## Add images to the folder
for i in range(len(id)):
    shutil.move(path1 + files[i], path2 + sorten[i]+'/'+files[i])



