class piggybank:
    def __init__(self):
        self.coin1 = 0
        self.coin2 = 0
        self.coin5 = 0
        self.coin10 = 0

    def add1(self ,n):
        self.coin1 += n

    def add2(self ,n):
        self.coin2 += n

    def add5(self ,n):
        self.coin5 += n

    def add10(self ,n):
        self.coin10 += n

    def __int__(self):
        return self.coin1 + self.coin2*2 + self.coin5*5 + self.coin10*10

    def __lt__(self ,rhs):
        return int(self) < int(rhs)

    def __str__(self):
        return '{1:' + str(self.coin1) + ', 2:' + str(self.coin2) + ', 5:' + str(self.coin5) + ', 10:' + str(self.coin10) + '}'

cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank() 
for c in cmd1: eval(c)
for c in cmd2: eval(c)