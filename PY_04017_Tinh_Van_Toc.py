class VanToc:
    def __init__(self, id, ten, donvi, vedich):
        self.id = id
        self.ten = ten
        self.donvi = donvi
        self.vedich = vedich
        self.tinh()
    
    def tinh(self):
        self.tg = self.vedich - 360
        self.tg /= 60.0
        self.vt = 120.0 / self.tg
        
    def inra(self):
        return f"{self.id} {self.ten} {self.donvi} {round(self.vt)} Km/h"

vantoc = []
for t in range(int(input())):
    ten = input().split()
    donvi = input().split()
    thoigian = input()
    
    # tao id
    id = ""
    for i in range(len(donvi)):
        id += donvi[i][0]
    for i in range(len(ten)):
        id += ten[i][0]
    ten = " ".join(ten)
    donvi = " ".join(donvi)
    
    # doi thoi gian
    vedich = int(thoigian[0]) * 60 + int(thoigian[2:4])
    
    vt = VanToc(id, ten, donvi, vedich)
    vantoc.append(vt)
    
vantoc.sort(key=lambda x: -x.vt)
for vt in vantoc:
    print(vt.inra())