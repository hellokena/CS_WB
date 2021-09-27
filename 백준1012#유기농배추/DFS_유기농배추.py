#백준1012_유기농배추
#DFS
import sys
sys.setrecursionlimit(10000)

def dfs(hidx, widx):
    graph[hidx][widx] = 0 # 방문 처리
    #상하좌우 방향벡터
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]
    for i in range(4):
        nh = hidx + dh[i]
        nw = widx + dw[i]
        if 0<=nh<n and 0<=nw<m and graph[nh][nw]==1:
            dfs(nh,nw)

def solution():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)

t = int(sys.stdin.readline().rstrip()) # 테스트 케이스
for _ in range(t):
    m,n,d = map(int, sys.stdin.readline().rstrip().split()) # 가로,세로,위치
    graph = [[0]*m for _ in range(n)]
    for _ in range(d):
        y,x = map(int, sys.stdin.readline().rstrip().split()) # 주의
        graph[x][y] = 1 # 배추 위치
    solution()
