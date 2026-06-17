from math import sqrt
import sys

class Triangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def tamgiac(self, other1, other2):
        d = (other1.x - self.x) * (other2.y - self.y) - (other2.x - self.x) * (other1.y - self.y)
        if d == 0:
            return "INVALID"
        else:
            ab = sqrt((other1.x - self.x)**2 + (other1.y - self.y)**2)
            ac = sqrt((other2.x - self.x)**2 + (other2.y - self.y)**2)
            bc = sqrt((other2.x - other1.x)**2 + (other2.y - other1.y)**2)
            return "{:.3f}".format(ab + ac + bc)
    
inputt = sys.stdin.read().split()
t = int(inputt[0])
i = 1
while t > 0:
    d1 = Triangle(float(inputt[i]), float(inputt[i + 1]))
    d2 = Triangle(float(inputt[i + 2]), float(inputt[i + 3]))
    d3 = Triangle(float(inputt[i + 4]), float(inputt[i + 5]))
    print(d1.tamgiac(d2, d3))
    i += 6
    t -= 1