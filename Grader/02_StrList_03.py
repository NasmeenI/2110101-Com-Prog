s = input()

l = s.split("/")
months = ["January" ,"February" ,"March" ,"April" ,"May" ,"June" ,"July" ,"August" ,"September" ,"October" ,"November" ,"December"]
print(months[int(l[1])-1] + ' ' + l[0] + ', ' + l[2])