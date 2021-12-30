# 거꾸로 별찍기
def solution(n):
    for i in range(n, 0, -1):
        print('*' * i)

n = int(input())
solution(n)
