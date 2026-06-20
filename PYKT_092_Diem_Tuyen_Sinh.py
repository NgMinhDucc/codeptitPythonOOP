def DanToc(dantoc):
    if dantoc != "Kinh":
        return 1.5
    return 0

def KhuVuc(khuvuc):
    if khuvuc == "1":
        return 1.5
    elif khuvuc == "2":
        return 1
    return 0

class TuyenSinh:
    def __init__(self, id, ten, diem, dantoc, khuvuc):
        self.id = "TS{:02d}".format(id)
        self.ten = ten
        self.diem = diem + DanToc(dantoc) + KhuVuc(khuvuc)
        self.danhgia()
    
    def danhgia(self):
        if self.diem >= 20.5:
            self.hang = "Do"
        else:
            self.hang = "Truot"
    
    def inra(self):
        return f"{self.id} {self.ten} {self.diem} {self.hang}"
    
tuyensinh = []    
for t in range(int(input())):
    ten = input().split()
    for i in range(len(ten)):
        ten[i] = ten[i].capitalize()
    ten = " ".join(ten)
    diem = float(input())
    dantoc = input()
    khuvuc = input()
    
    ts = TuyenSinh(t + 1, ten, diem, dantoc, khuvuc)
    tuyensinh.append(ts)
    
tuyensinh.sort(key=lambda x: -x.diem)
for ts in tuyensinh:
    print(ts.inra())