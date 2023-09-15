m = input()
n = int(input())

x = n - len(m)
if x > 0:
    print('0'*x,end='')
print(m)