from oob_api import generate

iterations = 100

res = generate('')
print(res)
# with open('output.txt', 'a') as f:
#     for i in range(0, iterations):
#         f.write(res + '\n')