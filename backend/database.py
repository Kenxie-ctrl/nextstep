import json
import os


def load_data(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except:
            return []
    return []


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
