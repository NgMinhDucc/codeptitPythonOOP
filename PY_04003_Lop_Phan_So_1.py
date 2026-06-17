from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        
    def rutgon(self):
        g = gcd(self.tu, self.mau)
        self.tu //= g
        self.mau //= g
        return f"{self.tu}/{self.mau}"
    
arr = input().split()
ps = PhanSo(int(arr[0]), int(arr[1]))
print(ps.rutgon())