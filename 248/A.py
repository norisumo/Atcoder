S = input()

sl = set()
for s in S:
    sl.add(int(s))

for i in range(10):
    if i in sl:
        continue
    print(i)