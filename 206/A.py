import decimal
N = int(input())

a = int(N * decimal.Decimal("1.08"))
if a < 206:
    print("Yay!")
elif a > 206:
    print(":(")
else:
    print("so-so")