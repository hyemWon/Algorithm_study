# 열 개씩 끊어 출력하기
# 알파벳 대소문자로 이루어진 길이가 N인 단어
# 한 줄에 10글자씩 끊어서 출력

from sys import stdin
from collections import deque
stdin = open("input.txt", 'r')

# deque 이용
def cut_string(arr):
    arr = deque(arr)
    while len(arr)>=10:
        for i in range(10):
            print(arr.popleft(), end='')
        print()
    else:
        for x in arr:
            print(x, end='')

if __name__=="__main__":
    arr = list(map(str, stdin.readline()))
    cut_string(arr)

str = stdin.readline()

# 인덱싱 이용
# for i in range(0, len(str), 10):
#     print(str[i:i+10])

# 인덱스 연산
# tmp = ''
# for i in range(len(str)):
#     tmp += str[i]
#     if (i+1)%10==0:
#         print(tmp)
#         tmp=''
# if tmp:
#     print(tmp)
