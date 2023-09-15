x = int(input())
l = [] # n ,time
l1 = []
l2 = []
for i in range(x):
    s = [e for e in input().split()]
    if s[0] == "reset":
        n = int(s[1])
    elif s[0] == "new":
        print("ticket" ,n)
        l.append([n ,int(s[1])])
        n += 1
    elif s[0] == "next":
        print("call" ,l[0][0])
        l1.append(l[0])
        l.pop(0)
    elif s[0] == 'order':
        print("qtime" ,l1[len(l1)-1][0] ,int(s[1])-l1[len(l1)-1][1])
        l2.append(int(s[1])-l1[len(l1)-1][1])
        l1.pop(len(l1)-1)
    elif s[0] == "avg_qtime":
        sum = 0
        for e in l2:
            sum += e
        print("avg_qtime" ,round(sum/len(l2) ,4))