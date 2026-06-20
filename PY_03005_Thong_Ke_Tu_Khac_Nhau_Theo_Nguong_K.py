import sys, re

inn = sys.stdin.read().split()
n, k = int(inn[0]), int(inn[1])
for i in range(n):
    text = " ".join(inn[2:])
    words = re.split(r"[^a-z0-9]", text.lower())
    thongke = {}
    for w in words:
        if w != "":
            if thongke.get(w) == None:
                thongke[w] = 1
            else:
                thongke[w] += 1

res = sorted(thongke, key=lambda x: (-thongke[x], x))
for i in res:
    if thongke[i] >= k:
        print(i, thongke[i])