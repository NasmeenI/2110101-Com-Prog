class member:
    def __init__(self ,name):
        self.name = name
        self.voted = 0
        self.ota_vote = list()
        self.camioshi = list()

    def vote_member(self ,ota ,voted):
        self.voted += voted
        if ota not in self.ota_vote: self.ota_vote.append(ota)

    def add_camioshi(self ,ota):
        self.camioshi.append(ota)

bnk48 = dict()
d_ota = dict()
while True:
    inp = input()
    if inp == '1' or inp == '2' or inp == '3': 
        st = inp
        break
    ota ,idol ,vote = inp.split()

    if idol not in bnk48: bnk48[idol] = member(idol)
    bnk48[idol].vote_member(ota ,int(vote))

    if ota not in d_ota: d_ota[ota] = dict()
    if idol not in d_ota[ota]: d_ota[ota][idol] = 0
    d_ota[ota][idol] += int(vote)

for key ,value in d_ota.items():
    mx = 0
    for key1 ,value1 in value.items():
        if mx < value1:
            mx = value1
            camioshi = key1
        elif mx == value1:
            camioshi = min(camioshi ,key1)
    bnk48[camioshi].add_camioshi(key)

new_bnk48 = list()
for key ,value in bnk48.items():
        new_bnk48.append(value)

if st == '1':
    new_bnk48 = sorted(new_bnk48 ,key=lambda x:x.voted ,reverse=True)
elif st == '2':
    new_bnk48 = sorted(new_bnk48 ,key=lambda x:len(x.ota_vote) ,reverse=True)
elif st == '3':
    new_bnk48 = sorted(new_bnk48 ,key=lambda x:len(x.camioshi) ,reverse=True)  

print(', '.join(new_bnk48[i].name for i in range(3)))