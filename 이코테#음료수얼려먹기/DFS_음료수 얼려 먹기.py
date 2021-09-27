# 음료수 얼려 먹기

## 기본 입력
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# visited 대신에 방문한 노드는 1로 변경
# visited = [[0]*m for _ in range(n)]

# 상하좌우
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]
cnt = 0

def dfs(h,w):
    graph[h][w] = 1 # 방문 처리
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if 0<=nh<n and 0<=nw<m and graph[nh][nw]==0:
            dfs(nh,nw)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i,j)
            cnt += 1 # 시작점 노드가 방문처리가 될때서야 cnt++

print(cnt)
