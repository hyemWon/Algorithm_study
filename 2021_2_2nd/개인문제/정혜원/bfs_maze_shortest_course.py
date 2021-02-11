# 미로의 최단거리 통로 (BFS 활용)
# 7*7 격자판 미로를 탈출하는 최단경로의 이동횟수 출력
# (1,1) -> (7,7)
# 벽: 1, 도로: 0
# 도착할 수 없으면 -1 출력

import sys
from collections import deque
# sys.stdin = open("input.txt", 'r')
MAX = 7
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

maze = [list(map(int, input().split())) for _ in range(MAX)]
maze[0][0]=1 # 체크리스트 대신 지나간 곳에 벽으로 만들어주면 같은 효과
dis = [[0]*MAX for _ in range(MAX)]
dQ = deque()
dQ.append((0,0))

L=0
while dQ:
    now = dQ.popleft()

    for j in range(4):
        x = now[0]+dx[j]
        y = now[1]+dy[j]
        # 격자판을 넘어가지 않으면서 벽이 아니면 데큐에 저장
        if 0<=x<MAX and 0<=y<MAX and maze[x][y]==0:
            maze[x][y]=1
            dis[x][y] = dis[now[0]][now[1]] + 1
            dQ.append((x,y))

res= dis[MAX-1][MAX-1]
if res==0:
    print(-1)
else:
    print(res)