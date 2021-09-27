# 미로 탈출
# 최단 경로는 bfs
# 간선비용 모두 같을 때 최단 경로 비용 비교 가능
from collections import deque

## 기본 입력값
n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 방향벡터
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def bfs(sh,sw):
    q = deque()
    q.append((sh,sw)) # 1. 큐에 시작 노드 삽입
    
    while q:
        ph, pw = q.popleft() # 2. 큐에서 pop
        for i in range(4):
            nh = ph + dh[i]
            nw = pw + dw[i]
            if 0<=nh<n and 0<=nw<m and graph[nh][nw] == 1: # 괴물이 없는부분이 1
                graph[nh][nw] = graph[ph][pw]+1 # 최단 경로를 구하는 것이므로 여러 갈래가 나올 수 있으니까
                q.append((nh, nw)) # 새로운 노드를 큐에 삽입한다
    print(graph[-1][-1])

bfs(0,0)
