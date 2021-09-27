import sys
from collections import deque

def solution():
    queue = deque([1]) # 첫 노드 삽입
    visited[1] = 1 # 및 방문 처리
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                # 루트 노드가 1
                # 그래프 탐색이므로 1부터 탐색한 다음에 
                # 다음 노드의 부모를 현재 노드로 설정해주면 됨
                parent[i] = node 
                queue.append(i) # 삽입 & 방문처리
                visited[i] = 1
    for p in range(2, n+1):
        print(parent[p])

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
visited=[0]*(n+1)
parent=[0]*(n+1)
for _ in range(n-1):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
solution()
