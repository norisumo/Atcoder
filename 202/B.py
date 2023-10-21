S = input()

d = {0:0, 1:1,6:9, 8:8,9:6}

for i in reversed(S):
    s = int(i)
    print(d[s],end = "")


print("")
