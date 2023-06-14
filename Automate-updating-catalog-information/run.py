#! /usr/bin/env python3

"""
Write a Python script named run.py to process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory.
The script should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name), and uploading it to http://[linux-instance-external-IP]/fruits using the Python requests library.
"""

import os
import requests

vm_ip="<vm_ip>"
url = f"http://{vm_ip}/fruits/"
text_src = "/home/{}/supplier-data/descriptions/".format(os.environ.get('USER'))

for file in os.listdir(text_src):

    print(file)

    with open(f"{text_src}/{file}","r+") as f:
        data = f.readlines()
        data_dict = {}
        print(data)

        for index,line in enumerate(data):
            # Each line is a different property => title,name,date,feedback
            if index == 0:
                    data_dict["name"] = line.rstrip()
            elif index == 1:
                    data_dict["weight"] = int(line.replace("lbs",""))
            elif index == 2:
                    data_dict["description"] = line.rstrip()

    data_dict["image_name"] = file.replace("txt","jpeg")

    print(data_dict)

    print("\n\n Attemping to Post...\n")
    try:
        r = requests.post(url, data=data_dict)
        print(f"STATUS_OK: {str(r.ok)}")
        print(f"RESPONSE_RAW: {r}")
        print(f"RESPONSE: {r.text}")
    except Exception as e:
        print(f"ERROR: {e}")
