def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0: 
            break
        x = t.strip().split() 
        if len(x) == 2: 
            return x[0], x[1]
    return "", ""

def compare_score(id1 ,id2):
    if id1[-2:] < id2[-2:]: return 1
    elif id1[-2:] > id2[-2:]: return 2
    else:
        if id1[:-2] < id2[:-2]: return 1
        elif id1[:-2] > id2[:-2]: return 2

file1 ,file2 = [e for e in input().split()]
file1 = '/Users/nasmeen/Documents/com_prog/Grader/' + file1 #?
file2 = '/Users/nasmeen/Documents/com_prog/Grader/' + file2 #?
infile1 = open(file1 ,"r") 
infile2 = open(file2 ,"r")

id1 ,score1 = read_next(infile1)
id2 ,score2 = read_next(infile2)i

while(True):
    if (id1 and score1) == "" and (id2 and score2) == "": break
    elif (id1 and score1) == "": ind = 2
    elif (id2 and score2) == "": ind = 1
    else: ind = compare_score(id1 ,id2)

    if ind == 1: 
        print(id1 ,score1)
        id1 ,score1 = read_next(infile1)
    elif ind == 2:
        print(id2 ,score2)
        id2 ,score2 = read_next(infile2)