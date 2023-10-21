from heapq import heappush, heappop

hq = []
sumNo = 0

Q = int(input())
for i in range(Q):
    s = input()
    n = int(s[0])
    if n == 1:
        x = int(s[2:])
        heappush(hq,x-sumNo)
    elif n == 2:
        x = int(s[2:])
        sumNo += x
    else:
        now = heappop(hq)
        print(now+sumNo)
