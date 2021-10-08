def solution(numbers, hand):
    answer = ''
    graph = {1 : [0, 0], 2 : [0, 1], 3 : [0, 2],
             4 : [1, 0], 5 : [1, 1], 6 : [1, 2],
             7 : [2, 0], 8 : [2, 1], 9 : [2, 2],
             '*' : [3, 0], 0 : [3, 1], '#' : [3, 2]} 
    
    posL = graph['*'] # 왼손 위치(*), [3, 0]
    posR = graph['#'] # 오른손 위치(#), [3, 2]
    
    for n in numbers:
        target = graph[n] # 누르고자 하는 번호의 좌표 위치
        
        if n in [1, 4, 7]: # 굳이 좌표로 표현하지 않고 숫자로 계산
            answer += 'L'
            posL = target # 왼손 위치 좌표로 초기화
            
        elif n in [3, 6, 9]: # 굳이 좌표로 표현하지 않고 숫자로 계산
            answer += 'R'
            posR = target # 오른손 위치 좌표로 초기화
            
        else: # [2, 5, 8, 0]
          
            # 거리 계산
            # posL/posR : 현재 위치, target : 누르고자 하는 위치 
            # X 좌표로 몇 칸 + Y 좌표로 몇 칸을 의미합니다. (피타고라스 계산 아님)
            distL = abs(posL[0]-target[0]) + abs(posL[1]-target[1])
            distR = abs(posR[0]-target[0]) + abs(posR[1]-target[1])
            
            if distL==distR: # 거리가 같을 경우
                if hand == 'left':# 왼손잡이
                    answer += 'L' # 왼손으로 누름
                    posL = target # 왼손 위치 초기화
                else: # 오른손잡이
                    answer += 'R' # 오른손으로 누름
                    posR = target # 오른손 위치 초기화
            
            elif distL < distR: # 왼손
                answer += 'L'
                posL = target
           
          else: # 오른손
                answer += 'R'
                posR = target
                
    return answer
