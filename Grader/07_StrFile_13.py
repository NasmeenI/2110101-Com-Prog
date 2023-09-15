s = input()
for ch in ['-' ,'"' ,"'" ,'(' ,')' ,'.' ,'>' ,':' ,';']: s = s.replace(ch ,' ')
s = [e for e in s.split()]

for i in range(len(s)):
    s[i] = s[i][0].upper() + s[i][1:].lower()
s[0] = s[0][0].lower() + s[0][1:]
print(''.join(map(lambda x:x ,[e for e in s])))