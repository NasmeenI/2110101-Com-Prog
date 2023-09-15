s = input()
score = []
for i in range(len(s)):
    if i < len(s) and s[i] == 'X':
        a = -1
        if i+1 < len(s) and '0' <= s[i+1] <= '9':
            if i+2 < len(s) and '0'<= s[i+2] <= '9':
                a = int(s[i+1]) + int(s[i+2])
            elif i+2 < len(s) and s[i+2] == '/':
                a = 10
        elif i+1 < len(s) and s[i+1] == 'X':
            if i+2 < len(s) and s[i+2] == 'X':
                a = 20
            elif i+2 < len(s) and '0'<= s[i+2] <= '9':
                a = 10 + int(s[i+2])
        if a != -1: score.append(10 + a)

    elif i < len(s) and '0'<= s[i] <= '9':
        a = -1
        if i+1 < len(s) and '0' <= s[i+1] <= '9':
            a = int(s[i]) + int(s[i+1])
            s = s[:i+1] + s[i+2:]
        elif i+1 < len(s) and s[i+1] == '/':
            if i+2 < len(s) and '0'<= s[i+2] <= '9':
                a = 10 + int(s[i+2])
            elif i+2 < len(s) and s[i+2] == 'X':
                a = 20 
        if a != -1: score.append(a)

x = int(input())
if 1 <= x <= 10:
    print(score[x-1])
else:
    sum = 0
    for e in score:
        sum += e
    print(sum)