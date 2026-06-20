import datetime, sys

class LichThi:
    def __init__(self, id, mamon, ds, ngaythi, giothi, nhom):
        self.id = "T{:03d}".format(id)
        self.mamon = mamon
        self.mon = ds[mamon]
        self.ngaythi = ngaythi
        self.giothi = giothi
        self.nhom = nhom
    
    def inra(self):
        return f"{self.id} {self.mamon} {self.mon} {self.ngaythi} {self.giothi} {self.nhom}"
    
n, m = map(int, input().split())
ds = {}
for i in range(n):
    ma = input()
    ds[ma] = input()

lichthi = []
for i in range(m):
    tt = input().split()
    mamon = tt[0]
    ngaythi = tt[1]
    giothi = tt[2]
    nhom = tt[3]
    
    lichthi.append(LichThi(i + 1, mamon, ds, ngaythi, giothi, nhom))

lichthi.sort(key=lambda x: (datetime.datetime.strptime(f"{x.ngaythi} {x.giothi}", "%d/%m/%Y %H:%M"), x.mamon))
for lt in lichthi:
    print(lt.inra())