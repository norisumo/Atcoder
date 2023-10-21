import math
import statistics

A = list(map(int, input().split()))
m = statistics.median(A)
print(m)
if m == A[1]:
    print("Yes")
else:
    print("No")