import math
n = int(input())

print("Yes" if n > 2*math.log2(n) else "No")
