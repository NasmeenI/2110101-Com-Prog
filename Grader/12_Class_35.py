class roman:
    def __init__(self ,r):
        self.value = 0
        d = {'I':1 ,'V':5 , 'X':10 ,'L':50 ,'C':100 ,'D':500 ,'M':1000}
        d1 = {'IV':4 ,'IX':9 ,'XL':40 ,'XC':90 ,'CD':400 ,'CM':900}
        for i in range(len(r)):
            if i == len(r)-1 or d[r[i]] >= d[r[i+1]]: self.value + d[r[i]]
            else: 
                self.value += d1[r[i]+r[i+1]]
                i += 1
            
    def __lt__(self ,rsh):
        return self.value < rsh.value

    def __str__(self):

