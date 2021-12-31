def fibonacci(n):
    if n == 0 or n == 1: return n
    else: return fibonacci(n-1) + fibonacci(n-2)

def solution(s):
    print(fibonacci(n))

n = int(input())
solution(n)
