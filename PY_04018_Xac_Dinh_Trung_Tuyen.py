class TrungTuyen:
    def __init__(self, id, ten, mamon, mauutien, tin, chuyenmon):
        self.id = "GV{:02d}".format(id)
        self.ten = ten
        self.mamon = mamon
        self.tong = tin * 2.0 + chuyenmon + mauutien
        self.danhgia()
        
    def danhgia(self):
        if self.tong >= 18.0:
            self.hang = "TRUNG TUYEN"
        else:
            self.hang = "LOAI"
    
    def inra(self):
        if self.mamon == "A":
            return f"{self.id} {self.ten} TOAN {self.tong} {self.hang}"
        elif self.mamon == "B":
            return f"{self.id} {self.ten} LY {self.tong} {self.hang}"
        else:
            return f"{self.id} {self.ten} HOA {self.tong} {self.hang}"
    
trungtuyen = []
for t in range(int(input())):
    ten = input()
    ma = input()
    mamon = ma[0]
    
    # phan loai ma uu tien
    mauutien = 0
    if ma[1] == "1":
        mauutien = 2.0
    elif ma[1] == "2":
        mauutien = 1.5
    elif ma[1] == "3":
        mauutien = 1.0
        
    tin = float(input())
    chuyenmon = float(input())
    
    tt = TrungTuyen(t + 1, ten, mamon, mauutien, tin, chuyenmon)
    trungtuyen.append(tt)
    
trungtuyen.sort(key=lambda x: -x.tong)
for tt in trungtuyen:
    print(tt.inra())