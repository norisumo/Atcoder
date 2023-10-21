L,R = map(int,input().split())
S = input()

re = S[L-1:R]
ans = S[:L-1] + re[::-1] + S[R:]


print(ans)