class ThoiGian:
    def __init__(self, id, ten, thoigianvao, thoigianra):
        self.id = id
        self.ten = ten
        self.thoigianchoi = abs(thoigianra - thoigianvao)
        self.tinh()
        
    def tinh(self):
        if self.thoigianchoi < 60:
            self.gio = 0
            self.phut = self.thoigianchoi
        else:
            self.gio = self.thoigianchoi // 60
            self.phut = self.thoigianchoi % 60
    
    def inra(self):
        return f"{self.id}  {self.ten} {self.gio} gio {self.phut} phut"
    
thoigian = []
for i in range(int(input())):
    id = input()
    ten = input()
    vao = input()
    thoigianvao = int(vao[0:2]) * 60 + int(vao[3:5])
    ra = input()
    thoigianra = int(ra[0:2]) * 60 + int(ra[3:5])
    
    tg = ThoiGian(id, ten, thoigianvao, thoigianra)
    thoigian.append(tg)
    
thoigian.sort(key=lambda x: (-x.gio, -x.phut))
for tg in thoigian:
    print(tg.inra())