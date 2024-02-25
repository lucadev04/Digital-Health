import os
import json

def create_config():
    file_exist = os.path.isfile("/home/luca/Luca/Privat/Python/digitalhealth/config.json")
    if file_exist == False:
        data = {
            "Theme": "dark",
            "Date": "lol",
        }
        jsondata = json.dumps(data, indent=2)
        with open("/home/luca/Luca/Privat/Python/digitalhealth/config.json", "w") as f:
            f.write(jsondata)
    else:
        print("config exists")
        return