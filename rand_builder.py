import random
f = open('rands', 'w')

for i in range(50000000):
    f.write(str(random.randint(0, 235885)) + "\n")
