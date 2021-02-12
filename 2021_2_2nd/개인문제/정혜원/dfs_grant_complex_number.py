# 단지 번호 붙이기 (DFS, BFS)
# 1은 집이 있는 곳, 0은 집이 없는 곳
# 상하좌우 연결된 집들의 모임을 단지로 정의하고 번호를 붙이려한다.
# 단지수와 각 단지에 속하는 집의 수를 오름차순 출력

import sys
# sys.stdin = open("input.txt", 'r')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    cnt += 1
    cp[x][y]=0
    for i in range(4):
        x_ = x+dx[i]
        y_ = y+dy[i]
        if 0<=x_<n and 0<=y_<n and cp[x_][y_]==1:
            DFS(x_, y_)


if __name__=="__main__":
    n = int(input())
    cp = [list(map(int, input())) for _ in range(n)]
    res = list() #각 단지의 집의 수

    for i in range(n):
        for j in range(n):
            if cp[i][j]==1:
                cnt = 0  #집의 수 계산
                DFS(i, j)
                res.append(cnt)
    
    print(len(res))
    for x in res:
        print(x)