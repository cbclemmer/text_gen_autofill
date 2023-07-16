import json
from oob_api import generate
from time import time
from datetime import datetime

iterations = 100

last_time = time()
generations = []
save_interval = 5
idx = 0
for i in range(0, iterations):
    idx += 1
    res = generate('', 300)
    generations.append(res)
    s_time = datetime.now().strftime("%H:%M:%S")
    diff_time = time() - last_time
    last_time = time()
    print(f'{s_time}: #{i} of {iterations}; {len(res)} characters generated in {diff_time:.2f}s')
    if idx % save_interval == 0:
        open('generations.json', 'w') as f:
            f.write(json.dumps(generations))
