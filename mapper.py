import sys 

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        store = data[2]
        price = data[4]
        print store + '\t' + price
