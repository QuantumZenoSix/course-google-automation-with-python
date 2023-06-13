#!/usr/bin/env python3

"""
Qwiklabs Assessment: Process Text Files with Python Dictionaries and Upload to Running Web Service
"""

import os
import requests

vm_ip="35.193.192.185"
path="/data/feedback"
url = f"http://{vm_ip}/feedback/"

for file in os.listdir(path):
    
    with open(f"{path}/{file}","r+") as f:
        data = f.readlines()
        data_dict = {}

        for index,line in enumerate(data):
            # Each line is a different property => title,name,date,feedback
            if index == 0:
                    data_dict["title"] = line
            elif index == 1:
                    data_dict["name"] = line
            elif index == 2:
                    data_dict["date"] = line
            elif index == 3:
                    data_dict["feedback"] = line

        print(data_dict)

        r = requests.post(url, data=data_dict)
        print(f"STATUS_OK: {str(r.ok)}")
        print(f"RESPONSE_RAW: {r}")
        #response = r.text
