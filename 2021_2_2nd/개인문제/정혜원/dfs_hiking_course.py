# 등산경로 (DFS)
# N*N 구역, 각 구역의 높이가 있다.
# 상, 하, 좌, 우 중에 더 높은 구역으로만 이동할 수 있도록 등산로 설계
# 가장 낮은 곳에서 출발, 가장 높은 곳으로

import sys
# sys.stdin = open("input.txt", 'r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x==ex and y==ey:
        cnt += 1
        return
    else:
        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            # 격자안에서 다음위치가 지나간 곳이 아니며 현재위치의 값보다 큰 경우
            if 0<=x_<n and 0<=y_<n and ch[x_][y_]==0 and h[x_][y_] > h[x][y]:
                    ch[x_][y_] = 1
                    DFS(x_, y_)
                    ch[x_][y_] = 0

    

if __name__=="__main__":
    n = int(input())
    h = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)] #들린 곳인지 확인
    cnt = 0 # 경로수

    # 출발지와 목적지 지정
    s = 2147000000
    e = -2147000000
    sx, sy = 0, 0
    ex, ey = 0, 0
    for i in range(n):
        for j in range(n):
            if h[i][j] < s:
                s = h[i][j]
                sx, sy = i, j
            if h[i][j] > e:
                e = h[i][j]
                ex, ey = i, j

    ch[sx][sy] = 1
    DFS(sx, sy)
    print(cnt)