# 세 수 중 두번째로 큰 수를 출력
def solution(arr):
    arr.sort()
    print(arr[1])

arr = list(map(int, input().split()))
solution(arr)
