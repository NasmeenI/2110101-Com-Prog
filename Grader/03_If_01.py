s = input()

if s.isdigit() and len(s)==2 and ((int(s)>=20 and int(s)<=40) or s=='51' or s=='53' or s=='55' or s=='58' or s=='01' or s=='02'):
    print("OK")
else:
    print("Error")