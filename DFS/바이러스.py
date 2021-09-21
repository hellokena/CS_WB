# 바이러스

n = int(input()) # 컴퓨터 갯수
m = int(input()) # 연결 쌍 갯수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x) # 무방향 그래프
visited = [0]*(n+1)
cnt = 0

def dfs(s):
    global cnt
    visited[s] = 1 # 방문 처리
    for i in graph[s]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1) # 1번 컴퓨터 부터 시작
# 시작점이 설정되어 있으므로 2중 for문 안 돌림
print(cnt)

