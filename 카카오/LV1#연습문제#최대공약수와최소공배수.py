def solution(n, m):
    answer = []
    
    # 최대공약수 # 나눠지는 수 중에 가장 큰 수
    for i in range(min(n,m),0,-1): # 최'대'공약수 이니까 반대로하는게 효율적
        if n%i == 0 and m%i == 0:
            answer.append(i)
            break
    
    # 최소공배수 # 곱셈 중에 가장 작은 수
    for j in range(max(n,m), (n*m)+1): # 스타트 수는 n,m 중에 큰 값 / 최댓값은 n*m
        if j%n == 0 and j%m == 0:
            answer.append(j)
            break
    
    return answer

# RE)
def solution(n, m):
    answer = []
    # 최대공약수
    for i in range(min(n,m), 0, -1):
        if n%i == 0 and m%i == 0:
            answer.append(i)
            break
    # 최소공배수
    for j in range(max(n,m), n*m+1):
        if j%n == 0 and j%m == 0:
            answer.append(j)
            break
    return answer
