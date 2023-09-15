fullname = ['Robert' ,'William' ,'James' ,'John' ,'Margaret' ,'Edward' ,'Sarah' ,'Andrew' ,'Anthony' ,'Deborah']
nickname = ['Dick' ,'Bill' ,'Jim' ,'Jack' ,'Peggy' ,'Ed' ,'Sally' ,'Andy' ,'Tony' ,'Debbie']
n = int(input())
for i in range(n):
    s = input()
    if s in fullname:
        print(nickname[fullname.index(s)])
    elif s in nickname:
        print(fullname[nickname.index(s)])
    else:
        print("Not found")