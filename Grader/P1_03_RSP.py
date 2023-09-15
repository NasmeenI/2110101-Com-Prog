m = int(input())
score_a = score_b = 0
cnt = 0
while True:
    if score_a == m:
        print(score_a ,score_b)
        print('Player 1 wins')
        break
    elif score_b == m:
        print(score_a ,score_b)
        print('Player 2 wins')
        break
    if cnt == 3*m:
        print(score_a ,score_b)
        print('Tie')
        break
    a ,b = [e for e in input().split()]
    if a=='R' and b=='S': score_a += 1
    elif a=='R' and b=='P': score_b += 1
    elif a=='S' and b=='R': score_b += 1
    elif a=='S' and b=='P': score_a += 1
    elif a=='P' and b=='R': score_a += 1
    elif a=='P' and b=='S': score_b += 1
    cnt += 1