# 에라토스테네스의 체
# 소수인지 판별하고 싶은 수의 제곱근 까지의 배수를 제외시켜주는 방법
def solution(n):
    answer = 0
    for i in range(2, n+1): # 2~n까지 # 1은 소수가 아니므로
        for j in range(2, int(i**0.5)+1): # 1과 자기 자신으로는 무조건 나눠짐
            if i%j == 0: # 나누어지는 수가 있으면 소수가 아님
                break
        else: # for-else문
            answer += 1
    return answer
