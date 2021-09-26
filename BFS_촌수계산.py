# 백준2644_촌수계산
from collections import deque
n = int(input()) # 사람수
parent, child = map(int, input().split())
r = int(input()) # 관계수
graph = [[]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
result = [0]*(n+1)
for _ in range(r):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def solution():
    global cnt
    queue = deque([parent])# 첫 노드 삽입
    visited[parent] = 1 # 첫 노드 방문 처리
    while queue:
        n = queue.popleft() # 노드 pop
        for i in graph[n]:
            if visited[i] == 0:
                queue.append(i) # 다음 노드 삽입 및 방문 처리
                visited[i] = 1
                result[i] = result[n]+1 # 각 노드 까지의 거리를 저장하는데, 전의 노드에서 하나가 이동했으므로 +1 해줌

    if result[child]==0: print(-1)
    else: print(result[child])

solution()
