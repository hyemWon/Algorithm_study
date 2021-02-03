# 수 정렬하기 (백준: 2750번)  -> 백준에서 시간초과 (다른방법 해보자.)
# N개의 수를 오름차순으로 정렬 (중복x)

from sys import stdin

# pivot 기준: 마지막 값
def quick_sort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = rt
        # pivot 기준 파티션
        for i in range(lt, rt):
            if arr[i] < arr[pivot]:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[pos], arr[pivot] = arr[pivot], arr[pos]
        quick_sort(lt, pos-1)
        quick_sort(pos+1, rt)

# pivot 기준: 처음 값
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     lt, rt = [], []
#     pivot = arr[0]
#
#     for i in range(1, len(arr)):
#         if arr[i] < pivot:
#             lt.append(arr[i])
#         else:
#             rt.append(arr[i])
#     return quick_sort(lt) + [pivot] + quick_sort(rt)


# 수 입력
if __name__=="__main__":
    N = int(stdin.readline())
    arr = [int(stdin.readline()) for _ in range(N)]
    # quick_sort(0, N-1)
    arr = quick_sort(arr)
    for x in arr:
        print(x)


