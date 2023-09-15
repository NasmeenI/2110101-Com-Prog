def knows(R ,x ,y):
    if y in R[x]: return True
    return False

def is_celeb(R ,x):
    celeb = True
    for k in R.keys():
        if k == x and not (R[k] == set() or R[k] == {k}): return False
        if k != x and not knows(R ,k ,x): celeb = False
    return celeb

def find_celeb(R):
    person = set()
    for k ,v in R.items():
        person.add(k)
        for e in v: person.add(e)

    for p in person:
        if is_celeb(R ,p): return p

def read_relations():
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1: break
        if d[0] not in R: R[d[0]] = {d[1]}
        else: R[d[0]].add(d[1])
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None: print('Not Found')
    else: print(c)

exec(input().strip())