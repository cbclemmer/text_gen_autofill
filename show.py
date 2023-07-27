import os
import json

if not os.path.exists('generations.json'):
    raise Exception('Could not find generations.json file')

f = open('generations.json', 'r', encoding='utf-8')
data = json.loads(f.read())
f.close()

for item in data:
    print(item)