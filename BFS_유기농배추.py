#백준1012_유기농배추
#BFS

import sys
from collections import deque

def solution():
    cnt = 0
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i,j]) # 첫 노드 삽입
                graph[i][j] = 0 # 후 방문 처리
                cnt += 1 # 첫 queue 완료하고 나서 cnt++
                while queue:
                    hidx, widx = queue.popleft()
                    dh = [-1, 1, 0, 0]
                    dw = [0, 0, -1, 1]
                    for d in range(4):
                        nh = hidx + dh[d]
                        nw = widx + dw[d]
                        if 0 <= nh < n and 0 <= nw < m and graph[nh][nw] == 1:
                            queue.append([nh,nw]) # 모든 노드 삽입 후
                            graph[nh][nw] = 0 # 방문 처리
    print(cnt)

t = int(sys.stdin.readline().rstrip()) # 테스트 케이스
for _ in range(t):
    m,n,d = map(int, sys.stdin.readline().rstrip().split()) # 가로,세로,위치
    graph = [[0]*m for _ in range(n)]
    for _ in range(d):
        y,x = map(int, sys.stdin.readline().rstrip().split()) # 주의
        graph[x][y] = 1 # 배추 위치
    solution()
