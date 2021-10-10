from itertools import permutations

def solution(numbers):
    
    answer = 0
    n = list(numbers) # 문자열을 각 숫자로 쪼갬
    length = len(n) # 숫자 갯수
    numbers = [] # 만들 수 있는 모든 수를 tuple 형식으로 저장
    numbers_int = [] # 만들 수 있는 모든 수를 int 형식으로 저장
    
    for i in range(1, len(n)+1):
        numbers.extend(list(permutations(n, i))) # 만들수 있는 모든 수 # append가 아닌 extend
        
    for j in numbers:
        numbers_int.append(int(''.join(j))) # 만들 수 있는 모든 수를 tuple->int
    numbers_int = list(set(numbers_int)) # 중복된 숫자 제외(11과 011은 같은 숫자로 취급)
    
    for l in numbers_int:
        if l == 0 or l == 1: continue # 1은 소수가 아님 # 0이라는 숫자가 만들어질수도 있음
        for k in range (2, int(l**0.5)+1): # 2~j # 에라토스테네스의 체
            if l%k == 0: break # 2~j 사이의 수에서 나눠지는 수가 있다는 것은 소수가 아님
        else: answer += 1 # for-else문 # 소수인 경우
          
    return answer
