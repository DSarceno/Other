import random
file = open('prueba.tsv','w')

for i in range(100):
    line = '{n1} \t {n2} \n'
    file.write(line.format(n1 = str(random.uniform(0,1000)), n2 = random.uniform(0,1000)))

file.close()
