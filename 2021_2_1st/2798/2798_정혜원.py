# 블랙잭
# N장의 카드에서 3장을 고른다.
# 카드의 합이 M을 넘지 않으면서 가장 큰 합을 만드는 게임
#

from sys import stdin
stdin = open("input.txt", 'r')

# 깊이탐색
def DFS(L, cnt, sum):
    global res
    if sum > m:
        return
    if cnt==3:
        if sum>res:
            res = sum
        return
    if L==n:
        return
    else:
        DFS(L+1, cnt+1, sum+card[L])
        DFS(L+1, cnt, sum)


if __name__=="__main__":
    n, m  = map(int, stdin.readline().split())
    card = list(map(int, stdin.readline().split()))
    res = -2147000000

    DFS(0,0,0)
    print(res)

