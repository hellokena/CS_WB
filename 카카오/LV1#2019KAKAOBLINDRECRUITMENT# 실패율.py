# 전체 스테이지 개수 N, 현재 사용자가 멈춰있는 스테이지 번호 배열 stages
def solution(N, stages):
    answer = {}
    users = len(stages) # 사용자 수
    for level in range(1, N+1): # 레벨1 ~ 레벨N
        if users == 0: # 0으로 나누어야 할 경우 # 런타임 에러 해결
            answer[level] = 0 
            continue
        count = stages.count(level) # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        answer[level] = count / users
        users -= count # 현재 스테이지에는 도달 했으나 다음 스테이지에 도달하지 못한 플레이어수만큼 빼준다
    return sorted(answer, key=lambda x:answer[x], reverse=True)
