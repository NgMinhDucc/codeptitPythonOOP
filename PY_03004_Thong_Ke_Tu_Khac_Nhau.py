import sys, re

inn = sys.stdin.read().split()
for i in range(int(inn[0])):
    text = " ".join(inn[1:])
    thongke = {}
    words = re.split("[^a-z0-9]", text.lower())
    for w in words:
        if w != "":
            if thongke.get(w) == None:
                thongke[w] = 1
            else:
                thongke[w] += 1
                
res = sorted(thongke, key=lambda x: (-thongke[x], x))
for i in res:
    print(i, thongke[i])