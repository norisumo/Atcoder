S = input()
ans = 0
for i in range(3):
    for j in range(3):
        ans += int(S[i]) * (10 ** j)


print(ans)