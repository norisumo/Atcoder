S = input()
ans = 0
l = len(S)
for i in range(l):
    s  = S[i]
    if s == '.':
        t = int(S[i+1])
        if t >= 5:
            n = ans % 10
            ans = ans // 10
            ans = ans * 10 + n + 1
        break
    else:
        ans = ans * 10 + int(s)


print(ans)