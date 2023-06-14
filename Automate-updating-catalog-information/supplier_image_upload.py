#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
student_id = "student-01-439710e8fd7b"
img_src = "/home/{}/supplier-data/images".format(student_id)

for file in os.listdir(img_src):

    img = "{}/{}".format(img_src,file)

    with open(img, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
