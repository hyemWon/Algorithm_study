# 알파코드 (DFS)
# 비밀편지를 암호화해서 주고받기
# A~Z : 1~26으로 암호화했을 때, 복호화하는 경우 몇 가지 결과?
# 0은 입력 종료

import sys
sys.stdin = open("input.txt", 'r')

def DFS(L):
    global cnt
    if L==n:
        cnt += 1
        for x in res:
            print(chr(x+64), end='')
        print()
        return
    else:
        for i in range(1, 26+1):
            # 한자리 수 씩
            if code[L]==i:
                res.append(i)
                DFS(L+1)
                res.pop()
            # 두자리
            elif i>=10 and L<n-1:
                if code[L]==i//10 and code[L+1]==i%10:
                    res.append(i)
                    DFS(L+2)
                    res.pop()


if __name__=="__main__":
    code = list(map(int, input()))
    n = len(code)

    # 0이 입력되면 입력 종료
    if n==1 and code[0]==0:
        sys.exit(0)
    else:
        res = list()
        cnt = 0
        DFS(0)
        print(cnt)
