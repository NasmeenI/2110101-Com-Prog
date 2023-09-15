num = {'0':'soon' ,'1':'neung' ,'2':'song' ,'3':'sam' ,'4':'si' ,'5':'ha' ,'6':'hok' ,'7':'chet' ,'8':'paet' ,'9':'kao'}
unit = ['' ,'sip' ,'roi' ,'pun']

def to_Thai(n):
    n = str(n)
    ans = list()
    for i in range(len(n)):
        a = num[n[i]]
        b = unit[-i+len(n)-1]
        if a == 'song' and b == 'sip': a = 'yi'
        if a == 'neung' and b == '' and len(n) > 1: a = 'et'
        if a == 'neung' and b == 'sip': a = ''
        if a == 'soon' and len(n) > 1: a = ''; b = ''
        
        if a != '': ans.append(a)
        if b != '': ans.append(b)
    ans1 = ' '.join(ans)
    return ans1

exec(input().strip())