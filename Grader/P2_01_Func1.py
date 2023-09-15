def is_odd(n):
    if n%2:
        return True
    else: return False

def has_odds(x):
    for e in x:
        if is_odd(e):
            return True
    return False

def all_odds(x):
    for e in x:
        if not is_odd(e):
            return False
    return True

def no_odds(x):
    for e in x:
        if is_odd(e):
            return False
    return True

def get_odds(x):
    ans = []
    for e in x:
        if is_odd(e):
            ans.append(e)
    return ans

def zip_odds(a, b):
    a = get_odds(a)
    b = get_odds(b)
    ind = 0
    ans = []
    while(1):
        if ind < len(a): ans.append(a[ind])
        if ind < len(b): ans.append(b[ind])
        ind += 1
        if ind >= len(a) and ind >= len(b): break
    return ans

exec(input().strip())