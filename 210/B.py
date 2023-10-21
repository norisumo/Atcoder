N = int(input())
S = input()

for i in range(N):
    s = S[i]
    if s == '1':
        if i % 2 == 0:
            exit(print("Takahashi"))
        else:
            exit(print("Aoki"))

