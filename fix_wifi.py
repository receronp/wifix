#!/usr/bin/python3
import os
import re
import json
import requests

data = {}
path = os.path.dirname(os.path.abspath(__file__))

html = requests.get(url="https://login.rz.ruhr-uni-bochum.de/cgi-bin/start").text
ip_rgx = re.search(r"(\d+.){3}\d+", html)

with open(path + "/data.json") as input_data:
    data = json.load(input_data)

response = requests.post(
    url="https://login.rz.ruhr-uni-bochum.de/cgi-bin/laklogin",
    data={
        "code": "1",
        "loginid": data["loginid"],
        "password": data["password"],
        "ipaddr": ip_rgx[0],
        "action": "Login",
    },
)

with open(path + "/response.html", "w") as output_file:
    output_file.write(response.text)
