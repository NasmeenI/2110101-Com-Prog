s = input()
l = s.split()
id_1 = l[0]
GPAX_1 = l[1]
comprog_1 = l[2]
cal1_1 = l[3]
cal2_1 = l[4]

s = input()
l = s.split()
id_2 = l[0]
GPAX_2 = l[1]
comprog_2 = l[2]
cal1_2 = l[3]
cal2_2 = l[4]

if (comprog_1 == 'A' and ('A' <= cal1_1 <= 'C') and ('A' <= cal2_1 <= 'C')) and (comprog_2 == 'A' and ('A' <= cal1_2 <= 'C') and ('A' <= cal2_2 <= 'C')):
    if(GPAX_1 == GPAX_2):
        if cal1_1 == cal1_2:
            if cal2_1 == cal2_2:
                print("Both")
            elif cal2_1 > cal2_2:
                print(id_2)
            elif cal2_1 < cal2_2:
                print(id_1)

        elif cal1_1 > cal1_2:
            print(id_2)
        elif cal1_1 < cal1_2:
            print(id_1)
    elif (GPAX_1 > GPAX_2):
        print(id_1)
    elif (GPAX_2 > GPAX_1):
        print(id_2)
elif (comprog_1 == 'A' and ('A' <= cal1_1 <= 'C') and ('A' <= cal2_1 <= 'C')):
    print(id_1)
elif (comprog_2 == 'A' and ('A' <= cal1_2 <= 'C') and ('A' <= cal2_2 <= 'C')):
    print(id_2)
else:
    print("None")