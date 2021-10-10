def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        tmp = []
        for a,b in zip(i,j):
            tmp.append(a+b)
        answer.append(tmp)
    return answer
