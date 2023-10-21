S = input()
Q = int(input())
ordA = ord('A')
for i in range(Q):
    t,k = map(int,input().split())
    k -= 1
    id = 0
    if t <= 60:
        id = k // (1 << t)
        k %= (1 << t)
    r = bin(k).count('1')
    l = t - r
    n = l + 2 * r
    ans = chr(((ord(S[id]) - ordA) + n) % 3 + ordA)
    print(ans)

