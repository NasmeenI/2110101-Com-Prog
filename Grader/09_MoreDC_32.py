def first_fit(L ,e):
    for e1 in L:
        if sum(e1) + e <= 100:
            e1.append(e)
            return L
    L.append([e])
    return L

def best_fit(L ,e):
    best = 100
    ind = -1
    for e1 in L:
        temp = sum(e1) + e
        if temp <= 100 and 100-temp < best:
            best = 100-temp
            ind = L.index(e1)
    if ind == -1: L.append([e])
    else: L[ind].append(e)
    return L

def partition_FF(D):
    ans = list()
    for e in D:
        ans = first_fit(ans ,e)
    return ans

def partition_BF(D):
    ans = list()
    for e in D:
        ans = best_fit(ans ,e)
    return ans

exec(input().strip())