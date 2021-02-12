# BFS 방법으로 풀이

import sys
from collections import deque
# sys.stdin = open("input.txt", 'r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
cp = [list(map(int, input())) for _ in range(n)]
cnt = 0
res = list()

dQ = deque()

for i in range(n):
    for j in range(n):
        if cp[i][j]==1:
            cnt = 1
            cp[i][j]=0
            dQ.append((i, j))
            # 하나의 구역 전부 검사
            while dQ:
                tmp = dQ.popleft()
                for k in range(4):
                    x = tmp[0]+dx[k]
                    y = tmp[1]+dy[k]
                    if 0<=x<n and 0<=y<n and cp[x][y]==1:
                        cnt += 1
                        cp[x][y]=0
                        dQ.append((x,y))
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)