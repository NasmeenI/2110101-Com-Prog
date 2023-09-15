import numpy as np

def spiral_square(n):
    l = [[0 for i in range(n+1)] for j in range(n+1)]
    i = n; j= n; cnt = n*n
    di = [0 ,-1 ,0 ,1]; dj = [-1 ,0 ,1 ,0]; st = 0
    while True:
        if l[i][j] != 0: break
        l[i][j] = cnt
        cnt -= 1
        i += di[st]
        j += dj[st]
        if i < 1 or i > n or j < 1 or j > n or l[i][j] != 0:
            i -= di[st]
            j -= dj[st]
            st = (st+1)%4
            i += di[st]
            j += dj[st]
            if i < 1 or i > n or j < 1 or j > n or l[i][j] != 0: break
    l = l[1:]
    for i in range(len(l)):
        l[i] = l[i][1:]
    return l

def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip())