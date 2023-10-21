import itertools

N = input()
l = len(N)
n = int(N)
ans = 0
#方針としては、n以下の全ての3,5,7を含む組み合わせに対して、全探索を行う

#Nの長さをlとし、3～lまでのループを回す(357が最小のため、3からになる)
for i in range(3,l+1):
    #itertoolsで直積を用いて全ての組み合わせを書き出す。
    t = set(itertools.product([3, 5, 7], repeat=i))
    for s in t:
        #求めた全ての組み合わせに対して文字列変換して結合する
        ss = "".join(map(str,s))
        #3,5,7全て入っているか？
        if "3" in ss and "5" in ss and "7" in ss:
            sn = int(ss)
            #n以下ならantを+1
            if sn <= n:
                ans += 1

print(ans)