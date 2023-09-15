s1 = sorted(''.join(map(lambda x:x ,[e for e in input().lower() if e != ' '])))
s2 = sorted(''.join(map(lambda x:x ,[e for e in input().lower() if e != ' '])))
if s1 == s2: print('YES')
else: print('NO')