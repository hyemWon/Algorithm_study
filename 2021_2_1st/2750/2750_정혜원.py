# 수 정렬하기 (백준: 2750번)
# N개의 수를 오름차순으로 정렬 (중복x)

from sys import stdin

# 병합정렬
def merge_sort(lt, rt):
    if lt<rt:
        # 리스트 반으로 나누기
        mid = (lt+rt)//2
        merge_sort(lt, mid)
        merge_sort(mid+1, rt)
        # 정렬하면서 합병
        p1 = lt
        p2 = mid+1
        tmp = list()
        while p1<=mid and p2<=rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1
        if p1<=mid: tmp = tmp + arr[p1:mid+1]
        if p2<=rt: tmp = tmp + arr[p2:rt+1]

        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]


# 수 입력
N = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(N)]
# quick_sort(0, N-1)
# arr = quick_sort(arr)
merge_sort(0, len(arr)-1)
for x in arr:
    print(x)
    
    
# 퀵정렬은 런타임 에러가 나서 병합정렬로 해줌
# pivot 기준: 마지막 값
# def quick_sort(lt, rt):
#     if lt < rt:
#         pos = lt
#         pivot = rt
#         # pivot 기준 파티션
#         for i in range(lt, rt):
#             if arr[i] < arr[pivot]:
#                 arr[i], arr[pos] = arr[pos], arr[i]
#                 pos += 1
#         arr[pos], arr[pivot] = arr[pivot], arr[pos]
#         quick_sort(lt, pos-1)
#         quick_sort(pos+1, rt)

# pivot 기준: 중앙 값
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



