def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        tmp = []
        for a,b in zip(i,j):
            tmp.append(a+b)
        answer.append(tmp)
    return answer

import numpy as np
def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    return (arr1+arr2).tolist()
