N = input()
l = len(N)
ans = ""
if l < 4:
    ans += "0" * (4-l) + N
else:
    ans = N


print(ans)