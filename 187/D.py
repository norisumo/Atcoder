N = int(input())
sa = 0
at = []
for i in range(N):
    a,b = map(int,input().split())
    sa += a
    at.append(a+b)
at.sort(reverse=True)


t = 0
cnt = 0
while sa >= t:
   sa -= at[cnt]
   cnt += 1 
print(cnt)


