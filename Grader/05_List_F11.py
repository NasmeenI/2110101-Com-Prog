def missing_digits(t):
    l1 = [0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
    l2 = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]
    ans = []
    for e in t:
        if e>='0' and e<='9' and int(e) in l1: l2[int(e)] += 1
    for i in range(len(l2)):
        if l2[i] == 0:
            ans.append(i)
    return ans

exec(input())