import csv
f = open('rands', 'r')

reader = csv.reader(f, delimiter='\n')

for row in reader:
    x = row
