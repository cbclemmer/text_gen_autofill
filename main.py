import os
import json
from oob_api import generate
import os
from time import time
from datetime import datetime

config = {}
if not os.path.exists('config.json'):
    print('Config file not found, going with default options')
    with open('config.json', 'r') as f:
        config = json.loads(f.read())

def get_with_default(param: str, default: any):
    if param in config:
        return config[param]
    return default

num_generations = get_with_default('num_generations', 100)
save_interval = get_with_default('save_interval', 5)
input_file = get_with_default('input_file', 'input.json')
use_input_file = get_with_default('use_input_file', True)
num_tokens = get_with_default('num_tokens', 300)
print_generation = get_with_default('print_generation', False)
prefix = get_with_default('prefix', '')

print(f"""
Config:
Prefix: {prefix}
Num Generations: {num_generations}
Save Interval: {save_interval}
Input File: {input_file}
Use Input File: {str(use_input_file)}
Num Tokens: {str(num_tokens)}
Print Generations: {str(print_generation)}
""")

last_time = time()
generations = []

if use_input_file:
    if not os.path.exists(input_file):
        raise Exception('Could not find input file ' + input_file)
    print('Found dataset file, reading...')
    dataset = []
    with open(input_file, 'r', encoding='utf-8') as f:
        dataset = json.loads(f.read())
    print(f'Input file found with {len(dataset)} inputs')
    if num_generations > len(dataset):
        num_generations = len(dataset)
    print(f'Running {num_generations} generations')
    for i in range(0, num_generations):
        prompt = f'{prefix}{dataset[i]}'
        res = generate(prompt, num_tokens)
        item = f'{prefix}{dataset[i]}\n{res}'
        generations.append(item)
        if print_generation:
            print(item)
        s_time = datetime.now().strftime("%H:%M:%S")
        diff_time = time() - last_time
        last_time = time()
        print(f'{s_time}: #{i} of {num_generations}; {len(res)} characters generated in {diff_time:.2f}s')
        if i % save_interval == 0:
            with open('generations.json', 'w') as f:
                f.write(json.dumps(generations))
else:
    print('No data file given, running generations with empty strings as input')
    for i in range(0, num_generations):
        res = generate(prefix, num_tokens)
        generations.append(res)
        if print_generation:
            print(res)
        s_time = datetime.now().strftime("%H:%M:%S")
        diff_time = time() - last_time
        last_time = time()
        print(f'{s_time}: #{i} of {num_generations}; {len(res)} characters generated in {diff_time:.2f}s')
        if i % save_interval == 0:
            with open('generations.json', 'w') as f:
                f.write(json.dumps(generations))