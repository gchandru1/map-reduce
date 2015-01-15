import sys

store_prev = ''
max_price = 0.0

for line in sys.stdin:
    store, price = line.strip().split('\t')
    if store != store_prev:
        if store_prev != '':
            print store_prev + '\t' + str(max_price)
        store_prev = store
        max_price = float(price)
    else:
        if float(price) > max_price:
            max_price = float(price)
else:
    print store + '\t' + str(max_price)