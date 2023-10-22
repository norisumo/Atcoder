S = input()
l = len(S)
ans = [0] * l
for i in range(l//2):
    ans[2*i+1] = S[2*i]
    ans[2*i] = S[2*i+1]
for i in range(l):
    print(ans[i], end='')
print("")