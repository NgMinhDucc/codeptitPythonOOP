import sys, re

text = sys.stdin.read()
sen = re.split(r"[.?!]", text) # tach chuoi tai ., ?, !, dong thoi loai bo cac ki tu nay khoi chuoi
for s in sen:
    s = " ".join(s.split())
    print(s.capitalize())