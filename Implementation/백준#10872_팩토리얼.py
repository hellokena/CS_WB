# 팩토리얼
def solution(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    print(answer)

n = int(input())
solution(n)

# ----------------

# 내장함수 사용
import math

def solution(n):
    print(math.factorial(n))

n = int(input())
solution(n)

# ----------------

# RecursionError
def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n-1)

def solution(n):
    print(factorial(n))

n = int(input())
solution(n)
