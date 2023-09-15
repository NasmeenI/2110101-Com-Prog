def grade_mcq(sol ,ans):
    if len(sol) != len(ans):
        return -1
    x = 0
    for i in range(len(sol)):
        if sol[i] == ans[i]:
            x += 1
    return x

exec(input())