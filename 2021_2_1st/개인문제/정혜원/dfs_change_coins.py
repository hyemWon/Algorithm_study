#  동전 바꿔주기 (DFS)
# 

import sys
# sys.stdin = open("input.txt", 'r')

def DFS(L, sum):
    global res
    if sum==T:
        res += 1
        return
    if L==k or sum > T:
        return
    else:
        for i in range(n[L]+1):
            DFS(L+1, sum+c[L]*i)

if __name__=="__main__":
    T = int(input()) #지폐금액
    k = int(input()) #동전 가지 수
    res = 0

    c = list()
    n = list()
    for i in range(k):
        a, b = map(int, input().split())
        c.append(a)
        n.append(b)
    
    DFS(0, 0)
    print(res)