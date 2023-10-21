N,Q = map(int,input().split())
S = input()
n = 0
for i in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        n = (n + x) % N
    elif t == 2:
        ai = (x-n+N) % N - 1
        print(S[ai])


