# 섬나라 아일랜드 (BFS 활용)
# 각 섬은 1로 표시되어 상하좌우와 대각선으로 연결
# 몇 개의 섬이 있는가?

import sys
from collections import deque
# sys.stdin = open("input.txt", 'r')

# 상하좌우 & 대각선
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0 #섬의 개수
dQ = deque()

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            dQ.append((i,j))
            cnt += 1
            arr[i][j]=0
            while dQ:
                tmp = dQ.popleft()
                for k in range(8):
                    x = tmp[0]+dx[k]
                    y = tmp[1]+dy[k]
                    if 0<=x<n and 0<=y<n and arr[x][y]==1:
                        dQ.append((x,y))
                        arr[x][y]=0
                       
print(cnt)