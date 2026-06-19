with open("DATA.in", "r") as f:
    data = f.readlines() # list of strings
    res = []
    for line in data:
        line = line.split()
        for l in line:
            try:
                if int(l) < -2**31 or int(l) > 2**31:
                    res.append(l)
            except ValueError:
                res.append(l)
    res.sort()
    print(*res)