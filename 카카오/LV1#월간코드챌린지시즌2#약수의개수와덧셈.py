def solution(left, right):
    answer = 0
    graph = {}
    for n in range(left, right+1): # left~right
        if n == 1: # 약수, 소수 문제에서는 항상 1을 고려하기
            graph[n] = 1
            continue
        graph[n] = 2 # 초기화 # 1과 자기자신
        for i in range(2, n): # 2~n-1
            if n%i==0: # 나누어진다면
                graph[n] += 1
    for k,v in graph.items():
        if v%2==0: answer += k
        else: answer -= k
    return answer

# 제곱수는 약수 갯수가 홀수이다
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
