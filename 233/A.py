x,y = map(int,input().split())

t = (y - x) 
ans = t // 10
if t <= 0:
    ans = 0
elif t % 10 != 0:
    ans += 1
print(ans)
