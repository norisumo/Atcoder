S = input()

for i in range(3):
    cnt = 0
    for j in range(3):
        if S[i] == S[j]:
            cnt += 1
    if cnt == 1:
        print(S[i])
        exit()
print(-1)