from re import A


def row_number(t ,e):
    for i in range(len(t)):
        if e in t[i]: return i

def flatten(t):
    ans = list()
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i][j] == 0: continue
            ans.append(t[i][j])
    return ans

def inversions(x):
    ans = 0
    for i in range(len(x)):
        for j in range(i+1 ,len(x)):
            if x[i] > x[j]: ans += 1
    return ans

def solvable(t):
    inversion = inversions(flatten(t))
    if len(t)%2 != 0 and inversion%2 == 0: return True
    elif len(t)%2 == 0:
        if inversion%2 != 0 and row_number(t ,0)%2 == 0: return True
        elif inversion%2 == 0 and row_number(t ,0)%2 != 0: return True
    return False

exec(input().strip())