import sys
n = int(sys.stdin.readline().rstrip())

def solution():
    result = 0
    for i in range(1, n+1):
        if i<100: result += 1
        else:
            temp = list(map(int, str(i)))
            if temp[1]-temp[0] == temp[2]-temp[1]: result += 1
    print(result)

solution()
