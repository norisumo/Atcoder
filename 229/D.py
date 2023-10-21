S = input()
K = int(input())
r = 0
now = 0
ls = len(S)
ans = 0
for l in range(ls):
    while r < ls:
        if S[r] == ".":
            if now == K:
                break
            else:
                now += 1
        r += 1
    ans = max(ans, r - l)
    
    if S[l] == '.':
        now -= 1

print(ans)
