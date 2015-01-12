import sys

store_prev = ''
price_prev = 0.0

for line in sys.stdin:
    store, price = line.strip().split('\t')
    if store != store_prev:
        if store_prev != '':
            print store_prev + '\t' + str(price_prev)
        store_prev = store
        price_prev = float(price)
    else:
        price_prev += float(price)
else:
    print store + '\t' + price