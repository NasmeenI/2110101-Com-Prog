mydict = {'X':0 ,'R':1 ,'Y':2 ,'G':3 ,'W':4 ,'B':5 ,'P':6 ,'K':7}
score = [0 ,0]
while True:
    s = input()
    if len(s) == 3: a ,b = s[1:3]
    else: a ,b = s[1] ,'X'
    score[int(s[0])-1] += mydict[a] + mydict[b]
    if s[1] == 'K': break
    
print(score[0] ,score[1])
if score[0] == score[1]: print('Tie')
elif score[0] > score[1]: print('Player 1 wins')
else: print('Player 2 wins')