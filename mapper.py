import sys 

for line in sys.stdin:
    line_list = line.strip().split("\t")
    store = line_list[2]
    price = line_list[4]
    print store + '\t' + price
