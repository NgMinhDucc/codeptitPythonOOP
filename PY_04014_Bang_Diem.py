import sys
from decimal import Decimal, ROUND_HALF_UP

class HocSinh:
    def __init__(self, id, ten, diem):
        if id < 10:
            self.id = "HS0" + str(id)
        else:
            self.id = "HS" + str(id)
        self.ten = ten
        tong = diem[0]*2 + diem[1]*2 + sum(diem[2:])
        self.tb = (Decimal(str(tong)) / Decimal("12")).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        self.xephang()
    
    def xephang(self):
        if self.tb >= 9.0:
            self.hang = "XUAT SAC"
        elif self.tb >= 8.0 and self.tb <= 8.9:
            self.hang = "GIOI"
        elif self.tb >= 7.0 and self.tb <= 7.9:
            self.hang = "KHA"
        elif self.tb >= 5 and self.tb <= 6.9:
            self.hang = "TB"
        else:
            self.hang = "YEU"
    
    def kq(self):
        # return f"{self.id} {self.ten} {int(self.tb*10) / 10} {self.hang}"
        return f"{self.id} {self.ten} {self.tb} {self.hang}"
        
inn = sys.stdin.read().splitlines()
idx = 1
hocsinh = []
for i in range(int(inn[0])):
    ten = inn[idx]
    idx += 1
    diem = [float(d) for d in inn[idx].split()]
    idx += 1
    hs = HocSinh(i + 1, ten, diem)
    hocsinh.append(hs)
    
hocsinh.sort(key=lambda x: (-float(x.tb), x.id))
for hs in hocsinh:
    print(hs.kq())