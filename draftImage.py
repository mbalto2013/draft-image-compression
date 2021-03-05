from PIL import Image
from pathlib import Path
import json
import PIL
import os
import glob

def imageStats(imageName):
    size=Path(imageName).stat().st_size
    return(size)

def statsComparisson(originalImage, newImage):
    return(-100*(1-(newImage/originalImage)))

def imageCompression(imageName):
    results = dict()
    originalWeight = imageStats(imageName)
    for quality in range(5, 96, 5):
        compressedImageName=f"{quality}_{imageName}"
        picture.save(compressedImageName,optimize=True,quality=quality)
        newWeight=imageStats(compressedImageName)
        results.update({compressedImageName: statsComparisson(originalWeight,newWeight)})
    
    return(json.dumps(results))

f = open("results.json", "a")
f.write(imageCompression("IMG_3444.jpg"))
f.close()
