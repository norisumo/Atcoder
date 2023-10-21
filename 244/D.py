S = list(input().split())
T = list(input().split())

for i in range(3):
    if S[0] == T[i] and S[1] == T[(i+1)%3] and S[2] == T[(i+2)%3]:
        exit(print("Yes"))
print("No")