class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'

    def getScore(self):
        if self.value == 'A': return 1
        elif self.value.isdigit(): return int(self.value)
        else: return 10

    def sum(self, other):
        return (self.getScore() + other.getScore())%10

    def __lt__(self, rhs):
        compare = {'3':3 ,'4':4 ,'5':5 ,'6':6 ,'7':7 ,'8':8 ,'9':9 ,'10':10 ,'J':11 ,'Q':12 ,'K':13 ,'A':14 ,'2':15 ,
                   'club':1 ,'diamond':2 ,'heart':3 ,'spade':4 }
        if self.value != rhs.value: return compare[self.value] < compare[rhs.value]
        else: return compare[self.suit] < compare[rhs.suit]

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])