def index(phalanxes ,name):
    for i in range(len(phalanxes)):
        if phalanxes[i].name == name: return i
    return -1

def f_vote(phalanxes ,name ,vote):
    for i in range(len(phalanxes)):
        for person ,x in phalanxes[i].person.items():
            if name == person:
                phalanxes[i].person[name] = vote
                return 

class phalanx:
    def __init__(self ,name):
        self.name = name
        self.person = dict()

    def add_person(self ,person):
        self.person[person] = 'Not Vote'

    def solve(self):
        vote_result = dict()
        for person ,vote in self.person.items():
            if vote == 'Not Vote': continue
            if vote not in vote_result: vote_result[vote] = 0
            vote_result[vote] += 1

        resolution = 'Inconclusive'
        mx = 0
        for vote ,num in vote_result.items():
            if mx < num:
                mx = num
                resolution = vote
            elif mx == num:
                resolution = 'Inconclusive'
        if resolution == 'Inconclusive': return ['Inconclusive']

        cobra = list()
        for person ,vote in self.person.items():
            if vote != 'Not Vote' and vote != resolution:
                cobra.append(person)

        cobra.sort()
        if len(cobra) == 0: return ['No cobra']
        return cobra

phalanxes = list()
for i in range(int(input())):
    phalanxes.append(phalanx(input()))

for i in range(int(input())):
    person ,pha = input().split()
    phalanxes[index(phalanxes ,pha)].add_person(person)

for i in range(int(input())):
    person ,vote = input().split()
    f_vote(phalanxes ,person ,vote)

for e in phalanxes:
    print(e.name)
    print(', '.join(e.solve()))