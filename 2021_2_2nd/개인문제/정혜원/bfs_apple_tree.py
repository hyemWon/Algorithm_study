# 사과나무 (BFS)
# 농장 N*N 격자판 (3<=N<=20: 홀수)
# 각 격자안에는 한 그루의 사과나무가 심어져 있다. 
# 다이아몬드 모양의 격자판의 사과나무만 수확한다.
# 수확하는 사과의 총 개수?

import sys
from collections import deque
# sys.stdin = open("input.txt", 'r')

# 시계방향 상 우 하 좌
dx = [-1, 0, 1, 0] #행
dy = [0, 1, 0, -1] #열

n = int(input())
apple = list()
for i in range(n):
    apple.append(list(map(int, input().split())))

ch=[[0]*n for _ in range(n)] #들렸는 곳인지 체크
sum = 0 # 사과의 총 개수 합

# 센터부터 시작
ch[n//2][n//2]=1 
sum += apple[n//2][n//2]

Q = deque()
Q.append((n//2, n//2)) #좌표 추가
L = 0
while True:
    if L==n//2:
        break
    size = len(Q)
    for i in range(size):
        now = Q.popleft()
        for j in range(4):
            x = now[0]+dx[j]
            y = now[1]+dy[j]
            if ch[x][y] == 0:
                ch[x][y] = 1
                sum += apple[x][y]
                Q.append((x, y))
    L+=1

print(sum)
    