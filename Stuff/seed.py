import random
import sys

n = int(sys.argv[1])

result_list = []
random.seed(n)

for i in range(3):
    result_list.append(random.randint(1,10))

print(result_list)
