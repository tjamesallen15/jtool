import json

import common.constants as consts

def load_data():
  config_file = open(consts.DATA_JSON)
  config_data = json.load(config_file)
  return config_data

def save_data(data):
  config_data = json.dumps(data, indent=4)
  with open(consts.DATA_JSON, "w") as outfile:
    outfile.write(config_data)