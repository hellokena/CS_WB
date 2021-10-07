import sys
from itertools import permutations
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
cards = []
for _ in range(n):
    cards.append(sys.stdin.readline().rstrip())
temp = set()
for n in permutations(cards,k):
    temp.add(''.join(n))
print(len(temp))
