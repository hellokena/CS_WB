import sys
n,m = map(int, sys.stdin.readline().rstrip().split())
card = list(map(int, sys.stdin.readline().rstrip().split()))

def solution():
    result = 0
    card.sort()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                temp = card[i]+card[j]+card[k]
                if temp <= m: result = max(temp, result)
    print(result)

solution()
