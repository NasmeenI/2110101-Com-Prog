class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'

    def next1(self):
        value = self.value
        suit = self.suit

        seq_value = ['3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' ,'J' ,'Q' ,'K' ,'A' ,'2']
        seq_suit = ['club' ,'diamond' ,'heart' ,'spade']
        if suit != seq_suit[-1]: suit = seq_suit[seq_suit.index(suit)+1]
        elif value != seq_value[-1]:
            value = seq_value[seq_value.index(value) + 1]
            suit = seq_suit[0]
        else:
            value = seq_value[0]
            suit = seq_suit[0]
        return Card(value ,suit)

    def next2(self):
        seq_value = ['3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'10' ,'J' ,'Q' ,'K' ,'A' ,'2']
        seq_suit = ['club' ,'diamond' ,'heart' ,'spade']
        if self.suit != seq_suit[-1]: self.suit = seq_suit[seq_suit.index(self.suit)+1]
        elif self.value != seq_value[-1]:
            self.value = seq_value[seq_value.index(self.value) + 1]
            self.suit = seq_suit[0]
        else:
            self.value = seq_value[0]
            self.suit = seq_suit[0]
        return self    

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])