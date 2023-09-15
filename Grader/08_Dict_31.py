def total(pocket):
    sum = 0
    for k ,v in pocket.items():
        sum += k*v
    return sum

def take(pocket ,money):
    for k ,v in money.items():
        if k in pocket: pocket[k] += v
        else: pocket[k] = v
    return pocket

def pay(pocket ,amt):
    cash = sorted(list(pocket) ,reverse = True)
    pays = dict()
    for k in cash:
        v = pocket[k]
        if k <= amt:
            if v >= amt//k:
                pays[k] = amt//k
                amt %= k
            else:
                pays[k] = v
                amt -= v*k
    if amt != 0: return set()
    for k ,v in pays.items():  pocket[k] -= v
    return pays

exec(input().strip())