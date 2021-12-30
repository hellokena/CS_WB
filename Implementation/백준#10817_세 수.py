def solution(arr):
    arr.sort()
    print(arr[1])

arr = list(map(int, input().split()))
solution(arr)
