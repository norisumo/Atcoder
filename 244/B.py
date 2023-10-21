N = int(input())
S = input()
dx = [1,0,-1,0]
dy = [0,-1,0,1]
now = [0,0,0]
for s in S:
    dir = now[2]
    x = now[0]
    y = now[1]
    if s == 'R':
        dir = (dir+1) % 4
    else:
        x = x + dx[dir]
        y = y + dy[dir]
    now = [x,y,dir]
print(now[0], now[1])
