from itertools import combinations
def solution(nums):
    answer = 0
    c = list(combinations(nums,3))
    for i in c:
        cnt = 0
        s = sum(i)
        print(s)
        for j in range(2, s): # 소수는 1과 자기자신만 약수로 가짐
            # 소수를 구하는 문제
            if s%j == 0: 
                cnt += 1
        if cnt==0: answer += 1
    return answer
 
# for-else문
# else문을 for문과 같은 줄에 쓰게되면, for문의 반복이 끝나고나서 else문이 실행되게 됩니다(break로 빠져나가지 않는다면) # 같은 수준의 들여쓰기 필요
    
from itertools import combinations
def solution(nums):
  answer = 0
  for c in combinations(nums, 3):
      temp = sum(c)
      for j in range(2, temp):
          if temp%j==0: # 나눠지는 수가 있으면
              break # 소수가 아님
      else:
          answer += 1
  return answer
