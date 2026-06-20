import sys, re

inn = sys.stdin.read().split()
for i in range(int(inn[0])):
    text = " ".join(inn[1:])
    words = re.split(r"[^a-z]", text.lower())
    thongke = {}
    for w in words:
        if w != "":
            if w not in thongke:
                thongke[w] = 1
            else:
                thongke[w] += 1

res = sorted(thongke, key=lambda x: (-thongke[x], x))
for i in res:
    print(i, thongke[i])