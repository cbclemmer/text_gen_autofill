import json

f = open('generations.json', 'r', encoding='utf-8')
data = json.loads(f.read())
f.close()

for item in data:
    print(item)