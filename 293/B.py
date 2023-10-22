N = int(input())
A = list(map(int, input().split()))

call = [0] * N
for i in range(N):
    if (call[i] == 0):
        call[A[i]-1] += 1

ans = 0
for i in range(N):
    if(call[i] == 0):
        ans += 1

print(ans)

for i in range(N):
    if (call[i] == 0):
        print(i+1, end=' ')
print("")