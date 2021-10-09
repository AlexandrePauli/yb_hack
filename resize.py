import os
from PIL import Image
import os
import PIL
import glob

path = 'data/Test1/full_sample/110_ferraie'
path2 = 'data/Test1/full_sample_resized/110_ferraie'


imgNames= os.listdir(path)

for imgName in imgNames:
    if imgName==".DS_Store":
        continue
    else:
        image = Image.open(path+'/'+imgName)
        image = image.resize(tuple([int(image.size[0]*0.85),int(image.size[1]*0.85)]))
        image.save(path2+'/'+imgName)


# Recréer les dossiers
path = "data/Images_3"
foldNames = os.listdir(path)

for foldName in foldNames:
    if foldName==".DS_Store":
        continue
    else:
        os.mkdir("data/Images_3_rescaled/"+foldName)

#########
path = "data/Images_3"
foldNames = os.listdir(path)

## LOOP to resize

for foldName in foldNames:
    if foldName ==".DS_Store":
        continue
    else:
        imgNames2 = os.listdir("data/Images_3_rescaled/" + foldName)
        if imgNames2 ==[]:
            imgNames = os.listdir("data/Images_3/"+foldName)
            for imgName in imgNames:
                if imgName == ".DS_Store":
                    continue
                else:
                    image = Image.open("data/Images_3/"+ foldName + "/" + imgName)
                    image = image.resize(tuple([int(image.size[0] * 0.85), int(image.size[1] * 0.85)]))
                    image.save("data/Images_3_rescaled/"+ foldName + "/" + imgName)
            print(foldName)
        else:
            print(foldName)
            continue




