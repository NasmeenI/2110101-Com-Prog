name ,num = [e for e in input().split()]
name = '/Users/nasmeen/Documents/com_prog/Grader/' + name #?
infile = open(name ,"r")

mn = 10000; mx = -1; mean = 0; n = 0
for line in infile:
    id ,score = line.split(); score = float(score)
    if id[:2] == num[-2:]:
        mn = min(mn ,score)
        mx = max(mx ,score)
        mean += score
        n += 1
if n == 0: print('No data')
else: print(mn ,mx ,mean/n)