P = list(map(int, input().split()))
ans = ""
oa = ord("a")
for p in P:
    ans += chr(oa + p - 1)
print(ans)
