#백준7576_토마토
#BFS
#인접한 토마토들을 다 queue에 넣어서 계산하여야하므로 BFS

import sys
from collections import deque

def solution():
    # 이미 다 익은 토마토인 경우에는 걸린날짜 0을 리턴해줄 수도 있음
    # 첫째날이 0일...
    cnt = -1 # 첫날은 day=0 # 첫날에 원래 익은 토마토 + 새로 익은 토마토 발생 # 첫날에도 익은 토마토 발생 **
    queue = deque() # 큐 선언

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1: # 처음에 익은 토마토 모두를 queue에 추가
                queue.append([i, j])
                # visited x
                # 원래 여기에 while queue가 와야 하는데, 모든 익은 토마토를 넣어주므로 identation이 달라짐

    while queue:
        cnt += 1 # 날짜 증가 # for문안에 넣어서는 안됨. 상하좌우가 하루만에 익기 때문
        for _ in range(len(queue)): # 한 회마다 queue안에 있는 모든 토마토를 계산해주어야함에 주의
            hidx, widx = queue.popleft()
            # 상하좌우 방향벡터
            dh = [-1, 1, 0, 0]
            dw = [0, 0, -1, 1]
            for d in range(4):
                nh = hidx + dh[d]
                nw = widx + dw[d]
                if 0<=nh<n and 0<=nw<m and graph[nh][nw] == 0: # 익지 않은 토마토이면
                    graph[nh][nw] = 1 # 익은 토마토로 만들어버림
                    queue.append([nh, nw])
    for g in graph:
        if 0 in g: # 익지 않은 토마토가 아직 존재함
            print(-1)
            return
    print(cnt)

m,n = map(int, sys.stdin.readline().rstrip().split()) # 가로, 세로
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
solution()
