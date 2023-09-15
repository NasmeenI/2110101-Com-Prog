def print_triangle(h):
    for i in range(h):
        for j in range(h+i):            
            if j==h-i-1 or j==h+i-1 or i==h-1:
                print('*' ,end='')
            else:
                print(' ' ,end='')
        print(end='\n')

exec(input())