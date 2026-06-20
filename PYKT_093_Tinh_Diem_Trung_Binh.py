from decimal import Decimal, ROUND_HALF_UP

def chuanhoa(ten):
    ten = ten.split()
    for i in range(len(ten)):
        ten[i] = ten[i].capitalize()
    return " ".join(ten)

class TinhDiem:
    def __init__(self, id, ten, d1, d2, d3):
        self.id = "SV{:02d}".format(id)
        self.ten = chuanhoa(ten)
        tong = (d1*3 + d2*3 + d3*2)
        self.diem = (Decimal(str(tong)) / Decimal("8")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.hang = 0
        
    def inra(self):
        return f"{self.id} {self.ten} {round(self.diem, 2)} {self.hang}"
    
tinhdiem = []
for i in range(int(input())):
    ten = input()
    d1, d2, d3 = float(input()), float(input()), float(input())
    
    td = TinhDiem(i + 1, ten, d1, d2, d3)
    tinhdiem.append(td)
    
tinhdiem.sort(key=lambda x: (-x.diem, x.id))
tinhdiem[0].hang = 1
for i in range(1, len(tinhdiem)):
    if tinhdiem[i].diem == tinhdiem[i - 1].diem:
        tinhdiem[i].hang = tinhdiem[i - 1].hang
    else:
        tinhdiem[i].hang = i + 1

for td in tinhdiem:
    print(td.inra())