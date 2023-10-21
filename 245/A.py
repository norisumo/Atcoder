A,B,C,D = map(int, input().split())

if A < C:
    print("Takahashi")
    exit()
if A == C:
    if B <= D:
        print("Takahashi")
        exit()



print("Aoki")
