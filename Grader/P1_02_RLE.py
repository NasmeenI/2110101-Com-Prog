def str2RLE():
    s = input()
    num = 1
    for i in range(len(s)):
        if i==len(s)-1 or s[i] != s[i+1]:
            print(s[i] ,num,end=' ')
            num = 1
        else:
            num += 1

def RLE2str():
    s = [e for e in input().split()]
    for i in range(0,len(s)-1,2):
        print(s[i]*int(s[i+1]),end='')

s = input()
if s == 'str2RLE':
    str2RLE()
elif s == 'RLE2str':
    RLE2str()
else:
    print('Error')