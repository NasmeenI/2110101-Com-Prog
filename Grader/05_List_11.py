s = input()
l1 = [0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
l2 = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]
ck = True
for e in s:
    if e>='0' and e<='9' and int(e) in l1: l2[int(e)] += 1
for i in range(len(l2)):
    if l2[i] == 0:
        if ck == True:
            print(i,end='')
            ck = False
        else: print(',' + str(l1[i]) ,end='')
if ck == True: print("None")