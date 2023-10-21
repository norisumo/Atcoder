N = int(input())
A = list(map(int, input().split()))
AC = list(range(1,N+1))
A.sort()
for i in range(N):
    if A[i] != AC[i]:
        exit(print("No")) 

print("Yes")