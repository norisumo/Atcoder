from collections import deque

N = int(input())
S = input()


#方針：Sを頭から1文字ずつチェックしていき、'x'以外の時はdequeに右から入れていく
#      'x'がきたらdequeのおしりからpopして2文字取り出して、"fox"を作れるかチェックする。
#      "fox"がつくれたらcontinue,作れなかったら3文字ともdequeに戻す。
#      Sを全てチェックしたらdequeの長さをチェックする。
q = deque()

for i in range(N):
    s = S[i]
    if s == 'x':
        isO = ''
        isF = ''
        if q:
            isO = q.pop()
        else:
            q.append(s)
            continue

        if q:
            isF = q.pop()
        else:
            q.append(isO)
            q.append(s)
            continue

        if isF == 'f' and isO == 'o':
            continue
        else:
            q.append(isF)
            q.append(isO)
            q.append(s)

    else:
        q.append(s)

ans = len(q)
print(ans)
