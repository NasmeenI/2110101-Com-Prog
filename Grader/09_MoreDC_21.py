from re import I


def factor(N):
    ans = list()
    i = 2
    while i <= N:
        if N%i != 0:
            i += 1
            continue
        j = 0
        while True:
            if N%i != 0: break
            N //= i
            j += 1
        ans.append([i ,j])
    return ans

exec(input().strip())