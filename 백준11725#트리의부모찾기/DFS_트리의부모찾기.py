import sys

def dfs(v):
    visited[v] = 1 # 방문처리
    for i in graph[v]:
        if visited[i] == 0: # 아직 방문 안했다면
            parent[i] = v # 현재 노드를 다음 노드의 부모로 설정
            dfs(i)
def solution():
    dfs(1)
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
