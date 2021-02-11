# 미로탐색 (DFS)
# 7*7 격자판 미로를 탈출하는 경로의 가지수 출력
# (1,1) -> (7,7)
# 1은 벽이고, 0은 통로이다. 상하좌우로만 움직인다.

import sys
# sys.stdin = open("input.txt", 'r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x==6 and y==6:
        cnt += 1
        print(cnt)
        return
    else:
        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if 0<=x_<7 and 0<=y_<7 and maze[x_][y_]==0:
                maze[x_][y_]=1
                DFS(x_,y_)
                maze[x_][y_]=0

if __name__=="__main__":
    maze = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    maze[0][0]=1
    DFS(0,0)
    print(cnt)
