def solution(d, budget):
    d.sort() # 작은것부터 더해줘야 많이 지원해줄 수 있음
    answer = 0
    now = 0 # 현재 사용된 예산
    for i in d:
        now += i # 각 예산을 더해본다
        if now <= budget: # 만약 돈이 더 들어가면(여유가 있다면)
            answer += 1 # 하나의 부서에 더 해줄 수 있는 것
        # 그렇지 않은 경우는 계속 그냥 for문만 도는 것
    return answer
