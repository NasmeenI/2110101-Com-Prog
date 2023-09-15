# A-Z 65-90
# a-z 97-122

def ROT_13(s):
    ans = []
    for e in s:
        if e == ' ': ans.append(' ')
        elif e >= 'A' and e <= 'Z':
            x = (ord(e) + 13)
            if x > 90: x -= 26
            ans.append(chr(x))
        elif e >= 'a' and e <= 'z':
            x = (ord(e) + 13)
            if x > 122: x -= 26
            ans.append(chr(x))
        else: ans.append(e)
    print(''.join(map(lambda x:x ,[e for e in ans])))

while(True):
    s = input()
    if s == 'end': break
    ROT_13(s)