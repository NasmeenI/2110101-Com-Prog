s = input()
if s[-2:] == 'ch' or s[-1:] == 'x' or s[-1:] == 's': s += 'es'
elif s[-1:] == 'y' and not s[-2:-1] in ['a' ,'e' ,'i' ,'o' ,'u']: s = s[:-1] + 'ies'
else: s += 's'

print(s)