f = open('/usr/share/dict/words', 'r')
n = open('rands', 'r')

x = []

for line in f:
    x.append(line)

bigdict = {}

for num in n:
    bigdict[str(x[int(num)])] = num

for num in n:
    y = bigdict[str(x[int(num)])]
