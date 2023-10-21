K = int(input())
h = K // 60
m = K % 60
ans = format(21 + h, '02d') + ":" + format(0 + m, '02d')
print(ans)