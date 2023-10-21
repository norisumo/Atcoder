N = input()
l = len(N)

l2 = 1 << (l-1)
ans = 0
for i in range(1,l2):
    s = []
    t = []
    for j in range(l):
        if i & (0x01 << j):
            s.append(int(N[j]))
        else:
            t.append(int(N[j]))

    s.sort(reverse=True)
    t.sort(reverse=True)

    si = 0
    for n in s:

        si = si * 10 + n
        
    ti = 0
    for n in t:

        ti = ti * 10 + n


    ans = max(ans, si*ti)

 
print(ans)
