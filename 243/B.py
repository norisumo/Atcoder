N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

same = 0
for i in range(N):
    if A[i] == B[i]:
        same += 1

print(same)

ans = 0
sa = set(A)
for b in B:
    if b in sa:
        ans += 1
print(ans-same)