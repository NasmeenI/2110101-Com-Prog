def RLE(t):
    ans = []
    num = 1
    for i in range(len(t)):
        if i==len(t)-1 or t[i] != t[i+1]:
            ans.append([t[i] ,num])
            num = 1
        else:
            num += 1
    return ans

exec(input())