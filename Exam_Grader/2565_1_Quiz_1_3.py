# 2565_1_Quiz_1_3 : 6532114921 Nasmeen Islam
# passworf for PDF : quiz_QUIZ

s = input()
s += '?'
x = []
ind = 0
for i in range(len(s)):
    if i == 0 and s[i] == '-': pass
    elif s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
        x.append(int(s[ind:i]))
        if s[i] == '-': ind = i
        else: ind = i + 1
    elif s[i] == '?':
        x.append(int(s[ind:i]))

sum = 0
for e in x: 
    sum += e
print(sum)
