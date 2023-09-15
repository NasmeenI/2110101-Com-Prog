def T2M(data):
    pattern = data[1]
    text = data[2:]
    for e1 in text:
        ans = ''
        for e in e1:
            j = pattern.find('[' + e + ']')
            if j == -1:
                print('Invalid :' ,e1)
                ans += 'error'
                break
            j += 3
            k = pattern.find('[',j)
            ans += pattern[j:k] + ' '
        if ans.find('error') == -1: print(ans)

def M2T(data):
    pattern = data[1]
    text = data[2:]
    for e1 in text:
        ans = ''
        e1 = e1.split(' ')
        for e in e1:
            j = pattern.find(']' + e + '[')
            if j == -1:
                print('Invalid :' ,' '.join(e1))
                ans += 'error'
                break
            k = pattern.find('[',j-2)
            ans += pattern[k+1:j]
        if ans.find('error') == -1: print(ans)

file = input()
infile = open(file ,"r")
data = infile.read()
data = data.split('\n')

if data[0] == 'T2M': T2M(data)
elif data[0] == 'M2T': M2T(data)
else: print('Invalid code')