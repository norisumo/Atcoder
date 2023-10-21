S1 = input()
S2 = input()

if S1[0] == S1[1] == "#":
    print("Yes")
    exit()
elif S1[0] == S2[0] == "#":
    print("Yes")
    exit()
elif S1[1] == S2[1] == "#":
    print("Yes")
    exit()
elif S2[0] == S2[1] == "#":
    print("Yes")
    exit()
print("No")