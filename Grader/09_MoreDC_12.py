n = int(input())
if n == 0: print('0\n0'); exit()
inte = {e for e in input().split()}
uni = set(inte)
for i in range(n-1):
    s = {e for e in input().split()}
    inte &= s
    uni |= s

print(len(uni))
print(len(inte))