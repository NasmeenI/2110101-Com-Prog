# 2565_2_Quiz_2_2 : 6532114921 Nasmeen Islam
# passworf for PDF : SECOND_quiz

def match(word, pattern, include_chars, exclude_chars):
    if len(word) != len(pattern): return False

    ck = True
    temp = ''
    for i in range(len(word)):
        if pattern[i] == '?': 
            if word[i] in exclude_chars: ck = False
            temp += word[i]
            continue
        if word[i] != pattern[i]: 
            ck = False
            break
    if not ck: return False

    for e in include_chars:
        ind = temp.find(e)
        if ind == -1: return False
        temp = temp[:ind] + temp[ind+1:]
    return True

exec(input())