def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= c
    return A

def mult(A ,B):
    ans = list()
    for i in range(len(A)):
        colum = list()   
        for j in range(len(B[0])):
            c = 0
            for k in range(len(B)):
                c += A[i][k]*B[k][j]
            colum.append(c)
        ans.append(colum)
    return ans

exec(input().strip())