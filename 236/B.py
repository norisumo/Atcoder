N = input()
A = list(map(int,input().split()))
t = [0] * N
for a in A:
    a -= 1
    t[a] += 1

for i in range(N):
    if t[i] == 3:
        print(i+1)