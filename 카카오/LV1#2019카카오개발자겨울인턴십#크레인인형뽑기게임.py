# 사라진 인형수 구하기
import numpy as np
def solution(board, moves):
    answer = 0
    board = np.transpose(board)
    basket = []
    for item in moves: # -1
        if board[item-1][-1] == 0: # 각 위치의 마지막 인형이 0인 경우 비어있다는 것
            continue # 인형이 없는 경우 아무일도 일어나지 않음
        else: # 마지막이 0이 아니라는 것은 인형이 하나라도 있다는 것
            for i in enumerate(board[item-1]):
                if i[1]!=0: 
                    temp = i[1] # 인형 뽑기
                    board[item-1][i[0]] = 0 # 인형 없어짐 처리 
                    break  
            basket.append(temp) # 바구니에 인형 추가
           # 인형 터뜨리기 
            index = 0
            while len(basket)>=2:
                if basket[index] == basket[index+1]: # 인형이 같으면
                    # 따로따로 터뜨리면 리스트 재조정으로 인해 리스트 달라짐
                    del basket[index:index+2] # 인형 터뜨림
                    answer += 2
                    index = 0
                    # 인형이 터뜨려진 경우 바구니 처음부터 다시 확인
                else: # 두 인형이 같지 않으면 우선 index++
                    index += 1
                    if index == len(basket)-1: break # 모든 바구니 탐색 끝  
    return answer
  
  # 간과한것
  # 1. transpose 할 필요없음
  # 2. stack해서 마지막것 두개만 비교하면 됨(굳이 처음부터 다시 비교 안해도됨) => 시간 낭비
  => 아래 코드가 효율성에서 갑임
  
   def solution(board, moves):
    stack = []
    answer = 0

    for i in moves:
        for j in range(len(board)): # 5
            if board[j][i-1] != 0:
                stack.append(board[j][i-1]) # 인형 뽑기
                board[j][i-1] = 0 # 인형 뽑음 처리

                if len(stack) > 1: # 바구니에 인형이 2개 이상일 때 
                    if stack[-1] == stack[-2]: # 마지막 2개 인형만 확인하면 됨
                        del stack[-2:]
                        answer += 2     
                break # 마지막 인형만 뽑고 다음 move로 옮김
                # break 없으면 한 위치에 있는 인형 다 뽑아버림

    return answer
