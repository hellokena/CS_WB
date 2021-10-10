def solution(n):
    answer = ''
    div,mod = divmod(n,3)
    while True:
        answer += str(mod)
        if div == 0: # 더 이상 나누어지지 않음
            break
        div,mod = divmod(div,3)
    return int(answer,3)

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3) # 나머지를 계속 더해줌 # 3진수 변환과 reverse가 동시에 이루어진 결과
        n = n // 3 # 몫 다시 초기화 # 몫이 0이 될 경우에 자동으로 break 됨
    return int(tmp, 3) # 3진법을 10진법으로 변환
    
    # 두 코드의 시간복잡도는 동일함
