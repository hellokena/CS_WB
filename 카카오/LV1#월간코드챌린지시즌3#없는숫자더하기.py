def solution(numbers):
    # 0~9의 합
    temp = 1+2+3+4+5+6+7+8+9
    for i in numbers:
        temp -= i
    return temp
  
  # 더 간단한 코드
  def solution(numbers):
    # 0~9의 합
    temp = 1+2+3+4+5+6+7+8+9
    answer = temp - sum(numbers)
    return answer
