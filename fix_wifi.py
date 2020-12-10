#!/usr/bin/env python3
import json
import requests

data = {}
with open("data.json") as input_data:
    data = json.load(input_data)

response = requests.post(
    url="https://login.rz.ruhr-uni-bochum.de/cgi-bin/laklogin",
    data={
        "code": data["code"],
        "loginid": data["loginid"],
        "password": data["password"],
        "ipaddr": data["ipaddr"],
        "action": data["action"],
    },
    headers={"accept": "application/json"},
)

with open("response.html", "w") as output_file:
    output_file.write(response.text)
