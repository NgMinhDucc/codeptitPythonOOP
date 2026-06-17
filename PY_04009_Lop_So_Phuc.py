import sys

class SoPhuc:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def tinhtoan(self):
        thuc = self.a + self.c
        ao = self.b + self.d
        
        # c = (a + b) * a
        cthuc = thuc * self.a - ao * self.b
        cao = thuc * self.b + ao * self.a
        if cao < 0:
            print(f"{cthuc} - {abs(cao)}i,", end=" ")
        else:
            print(f"{cthuc} + {cao}i,", end=" ")
        
        # d = (a + b)^2
        dthuc = thuc**2 - ao**2
        dao = 2 * thuc * ao
        if dao < 0:
            print(f"{dthuc} - {abs(dao)}i")
        else:
            print(f"{dthuc} + {dao}i")        
        
        
inn = sys.stdin.read().split()
i = 1
for t in range(int(inn[0])):
    a = inn[i]
    b = inn[i + 1]
    c = inn[i + 2]
    d = inn[i + 3]
    sp = SoPhuc(int(a), int(b), int(c), int(d))
    sp.tinhtoan()
    i += 4