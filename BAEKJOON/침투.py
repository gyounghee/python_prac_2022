# 13565번 - 침투

## 풀이 1
# - 메모리 : 36616 KB  /  시간 : 912 ms

from collections import deque
from sys import *
input = stdin.readline

def BFS(x,y) :
    q = deque([[x,y]])
    while q :
        x,y = q.popleft()
        if x == r-1 : return 1
        if p[x][y] == 1 : continue
        p[x][y] = 1
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if xx >= r or xx < 0 or yy >= c or yy < 0 or p[xx][yy] == 1: continue
            q.append([xx,yy])
    return 0

dx, dy = [-1,1,0,0], [0,0,-1,1]
r, c = map(int, input().split())
p = [list(map(int, list(input().rstrip()))) for _ in range(r)]
res = 0

for i in range(c) :
    if p[0][i] == 0 :
        if BFS(0,i) == 1 :
            res = 1 ; break

print('YES' if res else 'NO')

