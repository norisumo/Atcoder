a = [0] * 4

for i in range(4):
    s = input()
    if s == "H":
        a[0] += 1
    elif s == "2B":
        a[1] += 1
    elif s == "3B":
        a[2] += 1
    elif s == "HR":
        a[3] += 1
ans = "Yes"
for i in range(4):
    if a[i] != 1:
        ans = "No"
print(ans)