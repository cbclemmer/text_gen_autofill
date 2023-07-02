from oob_api import generate
from time import time
from datetime import datetime

iterations = 100

last_time = time()

for i in range(0, iterations):
    res = generate('', 300)
    s_time = datetime.now().strftime("%H:%M:%S")
    diff_time = time() - last_time
    last_time = time()
    print(f'{s_time}: #{i} of {iterations}; {len(res)} characters generated in {diff_time:.2f}s')
    with open('output.txt', 'a') as f:
        f.write(res + '\n')