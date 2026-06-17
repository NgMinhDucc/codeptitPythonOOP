from math import gcd
import sys

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        
    def tong(self, other):
        # tim mau so chung
        msc = self.mau // gcd(self.mau, other.mau) * other.mau
        # quy dong
        ts1 = msc // self.mau
        ts2 = msc // other.mau
        self.tu *= ts1
        other.tu *= ts2
        # tinh tong va rut gon
        rtu = self.tu + other.tu
        g = gcd(rtu, msc)
        rtu //= g
        msc //= g
        return f"{rtu}/{msc}"

arr = sys.stdin.read().split()
ps1 = PhanSo(int(arr[0]), int(arr[1]))
ps2 = PhanSo(int(arr[2]), int(arr[3]))
print(ps1.tong(ps2))