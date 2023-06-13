#!/usr/bin/env python3 

"""
Qwiklabs Assessment: Scale and convert images using PIL
"""

from PIL import Image import os 

for file in os.listdir("./images"): 
    try: 
        img = Image.open("./images/" + file).convert("RGB") #print(img) new img = img.resize((128,128)).rotate(90) new img.save("images2/" + file + ".jpeg") 
    except: 
        print("Skipping: " + file) 
