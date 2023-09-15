s = input()
for i in range(len(s)):
    if s[i] == '(':
        s = s[0:i] + '[' + s[i+1:len(s)]
    elif s[i] == '[':
        s = s[0:i] + '(' + s[i+1:len(s)]
    elif s[i] == ')':
        s = s[0:i] + ']' + s[i+1:len(s)]
    elif s[i] == ']':
        s = s[0:i] + ')' + s[i+1:len(s)] 
print(s)