# 양팔저울 (DFS)
# 1부터 S사이의 정수 중 측정이 불가능한 물의 무게는 몇가지?

import sys
# sys.stdin = open("input.txt", 'r')

def DFS(L, sum):
    global res
    if L==k:
        if 0<sum<=s:
            res.add(sum)
        return
    else:   
        DFS(L+1, sum+w[L])
        DFS(L+1, sum-w[L])
        DFS(L+1, sum)


if __name__=="__main__":
    k = int(input()) #추의 개수
    w = list(map(int, input().split())) #추의 무게 리스트
    s = sum(w)
    res = set()

    DFS(0, 0)
    print(s-len(res))
    