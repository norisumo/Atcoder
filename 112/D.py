N,M = map(int,input().split())

# 答えが最大になるのは N*s = Mとなるs
s = M // N

ans = 1

# s以下でMを割り切れる数aが答えになる。
# x * a = Mとなり、このxはNよりも大になる(sはM//Nで、aはs以下なので)
# なのでxが求まれば後は適当にxになるように a * t　のtを割り振ればよい
for a in range(s,1,-1):
    if M % a == 0:
        ans = a
        break
print(ans)
