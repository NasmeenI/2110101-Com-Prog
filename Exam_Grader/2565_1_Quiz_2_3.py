# 2565_2_Quiz_2_3 : 6532114921 Nasmeen Islam (25/100)
# passworf for PDF : SECOND_quiz

file_color = '/Users/nasmeen/Documents/com_prog/Exam_Grader/' + input()
file_music = '/Users/nasmeen/Documents/com_prog/Exam_Grader/' + input()
infile_color = open(file_color ,'r')
infile_music = open(file_music ,'r')

color = list()
for line in infile_color:
    x = line.split()
    for e in x:
        color.append(e.lower())

temp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for line in infile_music:
    newline = ''
    for e in line:
        if e in temp: newline += e
        else: newline += ' '

    x = newline.split()
    for e in x:
        if e.lower() in color:
            ind = line.find(e)
            s = '<' + e.lower() + '>' + e + '</>'
            line = line[:ind] + s + line[ind+len(e):]
        
        else:
            for e1 in color:
                ind = e.find(e1)
                if ind == -1: continue
                s1 = e[ind:ind+len(e1)]
                
                s = e[:ind] + '<' + s1.lower() + '>' + s1 + '</>' + e[ind+len(e1):]
                line = line[:line.find(e)] + s + line[line.find(e)+len(e):]
                    
    print(line ,end='')