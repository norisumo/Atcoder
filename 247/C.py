from copy import deepcopy

N = int(input())

def func(S,n):
    ret = deepcopy(S)
    ret.append(n)
    ret += S    
    return ret

ans = [1]

for i in range(2,N+1):
    ans = func(ans,i)

print(*ans)