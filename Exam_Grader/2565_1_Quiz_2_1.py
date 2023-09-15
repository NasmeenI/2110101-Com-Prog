# 2565_2_Quiz_2_3 : 6532114921 Nasmeen Islam
# passworf for PDF : SECOND_quiz

d = dict()
d['AEILNORSTU'] = 1
d['DG'] = 2
d['BCMP'] = 3
d['FHVWY'] = 4
d['K'] = 5
d['JX'] = 8
d['QZ'] = 10
l = ['AEILNORSTU' ,'DG' ,'BCMP' ,'FHVWY','K' ,'JX' ,'QZ']
l1 = list()

x = input().split()
for e in x:
    ans = 0
    for e1 in e:
        for e2 in l:
            if e1 in e2:
                ans += d[e2]
    l1.append([-ans ,e])

l1.sort()
for e in l1:
    print(e[1] ,-e[0])