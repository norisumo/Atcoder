S = input()
T = input()

l = len(S)
ans = "Yes"
cnt = 0
i = 0
while i < l:
    if S[i] == T[i]:
        i += 1
        continue
    else:
        if cnt < 1:
            if i+1 < l and ((S[i+1] == T[i]) and (S[i] == T[i+1])):
                i += 2
                cnt += 1
                continue
        i += 1
    ans = "No"
print(ans)

