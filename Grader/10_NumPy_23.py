import numpy as np

def read_data():
    w = [float(e) for e in input().split()] 
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    score_sum = np.sum( (data[: , 1:] * weight) ,1)
    score_avg = np.mean(score_sum)
    if np.sum( score_sum < score_avg ):
        print(', '.join(map(str ,data[score_sum < score_avg][: ,0])))
    else: 
        print('None')

exec(input().strip())
