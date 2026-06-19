import sys

class MonThi:
    def __init__(self, ma, mon, hinhthuc):
        self.ma = ma
        self.mon = mon
        self.hinhthuc = hinhthuc
    
    def inra(self):
        return f"{self.ma} {self.mon} {self.hinhthuc}"
    
inn = sys.stdin.read().splitlines()
idx = 1
monthi = []
for _ in range(int(inn[0])):
    ma = inn[idx]
    mon = inn[idx + 1]
    hinhthuc = inn[idx + 2]
    
    mt = MonThi(ma, mon, hinhthuc)
    monthi.append(mt)
    idx += 3

monthi.sort(key=lambda x: x.ma)
for mt in monthi:
    print(mt.inra())