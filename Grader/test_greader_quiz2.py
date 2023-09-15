file = '/Users/nasmeen/Documents/com_prog/Grader/' + input()
infile = open(file ,'r')

s1 = input()
s2 = input()

for line in infile:
    l = 0
    s = list()
    st = list()
    ans = list()
    for i in range(len(line)):
        if line[i] != '/': continue
        s.append(line[l:i])
        if line[l-1] == '/' or l == 0: st.append(True)
        l = i+1

    for e in s:
        if len(e) != len(s1): continue
        ck = True
        for i in range(len(e)):
            if e[i] == '?': continue
            if e[i].upper() != s1[i].upper():
                ck = False
                break
        if ck and st[s.index(e)]: ans.append(e)

    for e in ans:
        ind = line.find(e)
        if (line[ind-1] == '/' or ind == 0) and line[ind+len(e)] == '/': 
            line = line[:ind] + s2 + line[ind+len(e):]
            continue
    print(line,end='')