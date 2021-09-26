import sys
n = int(sys.stdin.readline().rstrip())

def solution():
    for i in range(1, n+1):
        temp = list(map(int, str(i)))
        if i+sum(temp) == n:
            print(i)
            return 0
    print(0)

solution()
