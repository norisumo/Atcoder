X = input()
l = len(X)
int_X = int(X)
if l <= 2:
    print(X)
    exit()

s = int(X[0])
for i in range(s,10):
    for d in reversed(range(10)):
        ans = str(i)
        cnt = 1
        n = i
        while cnt <= l:
            end = False
            if cnt == l:
                if int(ans) >= int_X:
                    print(ans)
                    exit()

            ans += str(n-d)
            n -= d
            cnt += 1
            if n < 0:
                break
    for d in range(10):
        ans = str(i)
        cnt = 1
        n = i
        while cnt <= l:
            end = False
            if cnt == l:
                if int(ans) >= int_X:
                    print(ans)
                    exit()

            ans += str(n+d)
            n += d
            cnt += 1
            if 10 <= n:
                break

l += 1
ans = ""
for i in range(l):
    ans += '1'
print(ans)
