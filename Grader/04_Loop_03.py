s1 = input()
s2 = input()

if len(s1) != len(s2): print('Incomplete answer')
else:
    ans = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]: ans += 1
    print(ans)