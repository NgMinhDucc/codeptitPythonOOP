class HoaDon:
    def __init__(self, id, mathang, soluong, dongia, chietkhau):
        self.id = id
        self.mathang = mathang
        self.soluong = soluong
        self.dongia = dongia
        self.chietkhau = chietkhau
        self.tong = soluong * dongia - chietkhau
        
    def inra(self):
        return f"{self.id} {self.mathang} {self.soluong} {self.dongia} {self.chietkhau} {self.tong}"
    
hoadon = []    
for i in range(int(input())):
    id = input()
    mathang = input()
    soluong = int(input())
    dongia = int(input())
    chietkhau = int(input())
    
    hd = HoaDon(id, mathang, soluong, dongia, chietkhau)
    hoadon.append(hd)

hoadon.sort(key=lambda x: -x.tong)
for hd in hoadon:
    print(hd.inra())