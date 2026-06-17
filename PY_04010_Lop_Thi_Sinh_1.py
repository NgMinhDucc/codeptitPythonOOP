class ThiSinh:
    def __init__(self, ten, sinh, s1, s2, s3):
        self.ten = ten
        self.sinh = sinh
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        
    def inra(self):
        print(self.ten, self.sinh, "{:.1f}".format(self.s1 + self.s2 + self.s3))
        
ten = input()
sinh = input()
s1 = float(input())
s2 = float(input())
s3 = float(input())
thisinh = ThiSinh(ten, sinh, s1, s2, s3)
thisinh.inra()