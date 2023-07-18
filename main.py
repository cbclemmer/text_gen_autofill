import os
import json
from oob_api import generate
from time import time
from datetime import datetime

iterations = 100

last_time = time()

dataset = []
dataset_file = ''
dataset_key = 'input'
if os.path.exists(dataset_file):
    try:
        with open(dataset_file, 'r') as f:
            for item in json.loads(f.read()):
                dataset.append(item[dataset_key])
    except Exception as e:
        print(e)

if len(dataset) > 0:
    if iterations > len(dataset):
        iterations = len(dataset)
    for i in range(0, iterations):
        res = generate(dataset[i], 300)
        s_time = datetime.now().strftime("%H:%M:%S")
        diff_time = time() - last_time
        last_time = time()
        print(f'{s_time}: #{i} of {iterations}; {len(res)} characters generated in {diff_time:.2f}s')
        with open('output.txt', 'a') as f:
            f.write(res + '\n')
else:
    for i in range(0, iterations):
        res = generate('', 300)
        s_time = datetime.now().strftime("%H:%M:%S")
        diff_time = time() - last_time
        last_time = time()
        print(f'{s_time}: #{i} of {iterations}; {len(res)} characters generated in {diff_time:.2f}s')
        with open('output.txt', 'a') as f:
            f.write(res + '\n')