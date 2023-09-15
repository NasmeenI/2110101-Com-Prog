def pattern1(nrows ,ncols):
    cnt = 1
    ans = [[0 for j in range(ncols)] for i in range(nrows)]
    for i in range(nrows):
        for j in range(ncols):
            ans[i][j] = cnt
            cnt += 1
    return ans

def pattern2(nrows ,ncols):
    cnt = 1
    ans = [[0 for j in range(ncols)] for i in range(nrows)]
    for j in range(ncols):
        for i in range(nrows):
            ans[i][j] = cnt
            cnt += 1
    return ans

def pattern3(N):
    cnt = 1
    ans = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(i ,N):
            ans[i][j] = cnt
            cnt += 1
    return ans

def pattern4(N):
    cnt = 1
    ans = [[0 for j in range(N)] for i in range(N)]
    for j in range(N):
        for i in range(j+1):
            ans[j-i][j] = cnt
            cnt += 1
    return ans
    
def pattern5(N):
    cnt = 1
    ans = [[0 for j in range(N)] for i in range(N)]
    for j in range(N):
        for i in range(N-j):
            ans[i][i+j] = cnt
            cnt += 1
    return ans

def pattern6(N):
    cnt = 1
    ans = [[0 for j in range(N)] for i in range(N)]
    for j in range(N):
        if j%2 == 0:
            for i in range(N-j):
                ans[i][i+j] = cnt
                cnt += 1  
        else:    
            for i in range(N-j-1 ,-1 ,-1):
                ans[i][i+j] = cnt
                cnt += 1
    return ans

exec(input().strip())