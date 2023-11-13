import json
import os

import pandas as pd

try:
    os.remove("events.csv")
except Exception as e:
    print("Error on deleting file:",e)

chunks = pd.read_json('events.json', lines=True, chunksize=1000000)
# df = pd.read_json('events.json', lines=True, chunksize=200)
header = True
for chunk in chunks:
    json_struct = json.loads(chunk.to_json(orient="records"))
    df_flat = pd.json_normalize(json_struct)
    df_flat.to_csv('events.csv', header=header, encoding='utf-8', index=False, mode='a')
    header = False
