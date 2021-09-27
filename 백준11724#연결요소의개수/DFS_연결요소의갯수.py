import sys
sys.setrecursionlimit(10000) # 런타임에러 해결

n, m = map(int, sys.stdin.readline().rstrip().split()) # 시간초과 해결
#n,m = map(int, input().split()) # 노드, 간선
graph = [[]*(n+1) for _ in range(n+1)] # 노드 0은 비웠으므로, 아래에서 for문 돌릴 때는 1부터 돌림
visited = [0]*(n+1)
for _ in range(m):
    #x,y = map(int, input().split())
    x,y = map(int, sys.stdin.readline().rstrip().split()) # 시간초과 해결
    graph[x].append(y)
    graph[y].append(x)

def solution(): # dfs
    cnt = 0
    for i in range(1, n+1): # 시작점이 명시되어 있지 않음
        if visited[i] == 0:
            dfs(i)
            cnt += 1
    print(cnt)

def dfs(v):
    visited[v] = 1 # 방문 처리
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

solution()
