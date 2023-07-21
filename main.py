import os
import json
from oob_api import generate
from time import time
from datetime import datetime

iterations = 100

last_time = time()
generations = []
save_interval = 5

dataset = []
dataset_file = 'input.json'
dataset_key = 'input'
if os.path.exists(dataset_file):
    try:
        with open(dataset_file, 'r') as f:
            for item in json.loads(f.read()):
                data = item
                if dataset_key is not None:
                    data = item[dataset_key]
                dataset.append(data)
    except Exception as e:
        print(e)

if len(dataset) > 0:
    print(f'Input file found with {len(dataset)} inputs')
    if iterations > len(dataset):
        iterations = len(dataset)
    for i in range(0, iterations):
        res = generate(dataset[i], 300)
        generations.append(res)
        s_time = datetime.now().strftime("%H:%M:%S")
        diff_time = time() - last_time
        last_time = time()
        print(f'{s_time}: #{i} of {iterations}; {len(res)} characters generated in {diff_time:.2f}s')
        if i % save_interval == 0:
            with open('generations.json', 'w') as f:
                f.write(json.dumps(generations))
else:
    print('No input data found, sending empty strings')
    for i in range(0, iterations):
        res = generate('', 300)
        generations.append(res)
        s_time = datetime.now().strftime("%H:%M:%S")
        diff_time = time() - last_time
        last_time = time()
        print(f'{s_time}: #{i} of {iterations}; {len(res)} characters generated in {diff_time:.2f}s')
        if i % save_interval == 0:
            with open('generations.json', 'w') as f:
                f.write(json.dumps(generations))