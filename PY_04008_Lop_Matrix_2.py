import sys

class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a
        
    def nhan(self):
        # ma tran chuyen vi
        b = []
        for i in range(self.m):
            b.append([0] * self.n)
            for j in range(self.n):
                b[i][j] = self.a[j][i]
                
        # nhan ma tran
        c = []
        for i in range(self.n):
            c.append([0] * self.n)
            for j in range(self.n):
                for k in range(self.m):
                    c[i][j] += self.a[i][k] * b[k][j]
        
        # in ma tran            
        for i in range(self.n):
            for j in range(self.n):
                print(c[i][j], end=" ")
            print()

inn = sys.stdin.read().split()
idx = 1
for t in range(int(inn[0])):
    n, m = int(inn[idx]), int(inn[idx + 1])
    idx += 2
    a = []
    for i in range(n):
        a.append([0] * m)
        for j in range(m):
            a[i][j] = int(inn[idx])
            idx += 1
    
    ma = Matrix(n, m, a)
    ma.nhan()