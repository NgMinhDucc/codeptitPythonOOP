class HoaDon:
    def __init__(self, id, ten, tieuthu):
        self.id = "KH{:02d}".format(id)
        self.ten = ten
        self.tieuthu = tieuthu
        self.tinhhoadon()
        
    def tinhhoadon(self):
        if self.tieuthu <= 50:
            self.tong = self.tieuthu * 100
            self.tong *= 1.02
        elif self.tieuthu <= 100 and self.tieuthu >= 51:
            self.tong = 50 * 100 + (self.tieuthu - 50) * 150
            self.tong *= 1.03
        else:
            self.tong = 50 * 100 + 50 * 150 + (self.tieuthu - 100) * 200
            self.tong *= 1.05
        self.tong = round(self.tong)
        
        return f"{self.id} {self.ten} {self.tong}"
        
hoadon = []
for t in range(int(input())):
    ten = input()
    cu = int(input())
    moi = int(input())
    tieuthu = moi - cu
    
    hd = HoaDon(t + 1, ten, tieuthu)
    hoadon.append(hd)

hoadon.sort(key=lambda x: -x.tieuthu)
for hd in hoadon:
    print(hd.tinhhoadon())