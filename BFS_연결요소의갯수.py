from collections import deque
import sys # 시간초과 해결

#n,m = map(int, input().split()) # 노드, 간선
n, m = map(int, sys.stdin.readline().rstrip().split()) # 시간초과 해결
graph = [[]*(n+1) for _ in range(n+1)] # 노드 0은 비웠으므로, 아래에서 for문 돌릴 때는 1부터 돌림
visited = [0]*(n+1)
for _ in range(m):
    #x,y = map(int, input().split())
    x, y = map(int, sys.stdin.readline().rstrip().split()) # 시간초과 해결
    graph[x].append(y)
    graph[y].append(x)

def solution(): # dfs
    cnt = 0
    queue = deque() # 아직 첫 노드 몰라서 안 넣음
    for i in range(1, n+1): # 시작점이 명시되어 있지 않음
        if visited[i] == 0:
            queue.append(i) # 첫 노드를 넣음
            visited[i] = 1 # 첫 노드 방문 처리
            cnt += 1 # 연결 요소의 갯수를 구하는것 # 단지 갯수!
            while queue:
                now = queue.popleft()
                for next in graph[now]:
                    if visited[next] == 0:
                        queue.append(next) # 다음 노드 삽입
                        visited[next] = 1 # 후 방문처리
    print(cnt)

solution()

