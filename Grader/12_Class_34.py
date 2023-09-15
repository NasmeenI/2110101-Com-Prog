class piggybank:
    def __init__(self):
        self.coins = dict()
    
    def add(self ,v ,n):
        if self.sum() + n > 100: return False
        v = float(v)
        if v not in self.coins: self.coins[v] = 0
        self.coins[v] += n
        return True

    def __float__(self):
        sum = 0.0
        for key ,value in self.coins.items():
            sum += (key*value)
        return sum

    def __str__(self):
        seq_coins = list()
        for key ,value in self.coins.items():
            seq_coins.append(key)
        seq_coins.sort()

        ans = list()
        for coin in seq_coins:
            ans.append(str(coin) + ':' + str(self.coins[coin]))
        return '{' +  ', '.join(ans) + '}'
    
    def sum(self):
        sum = 0
        for key ,value in self.coins.items():
            sum += value
        return sum

cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank() 
for c in cmd1: eval(c)
for c in cmd2: eval(c)