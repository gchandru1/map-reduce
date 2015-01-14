import sys 

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        product = data[3]
        price = data[4]
        print product + '\t' + price
