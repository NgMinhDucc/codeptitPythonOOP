import sys

class XepHang:
    def __init__(self, ten, ac, sub):
        self.ten = ten
        self.ac = ac
        self.sub = sub
        
    def inra(self):
        return f"{self.ten} {self.ac} {self.sub}"
    
inn = sys.stdin.read().splitlines()
idx = 1
xephang = []
for t in range(int(inn[0])):
    ten = inn[idx]
    idx += 1
    bai = inn[idx].split()
    ac, sub = int(bai[0]), int(bai[1])
    idx += 1
    
    xh = XepHang(ten, ac, sub)
    xephang.append(xh)
    
xephang.sort(key=lambda x: (-x.ac, x.sub, x.ten))
for xh in xephang:
    print(xh.inra())