import sys

prod_prev = ''
price_prev = 0.0

for line in sys.stdin:
    prod, price = line.strip().split('\t')
    if prod != prod_prev:
        if prod_prev != '':
            print prod_prev + '\t' + str(price_prev)
        prod_prev = prod
        price_prev = float(price)
    else:
        price_prev += float(price)
else:
    print prod + '\t' + price