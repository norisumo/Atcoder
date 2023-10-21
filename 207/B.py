A,B,C,D = map(int, input().split())
 
if C*D -B < 1:
    print(-1)
    exit()
t = C * D - B
ans = A // t
if A % t != 0:
    ans += 1
print(ans)