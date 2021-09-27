#백준4963_섬의개수
#BFS

import sys
from collections import deque

def solution():
    cnt = 0
    # 북, 북동, 동, 남동, 남, 남서, 서, 북서 방향벡터
    dh = [-1, -1, 0, 1, 1, 1, 0, -1]
    dw = [0, 1, 1, 1, 0, -1, -1, -1]
    queue = deque() # 큐 선언
    for i in range(h): # 시작점이 명시되어 있지 않음
        for j in range(w):
            if graph[i][j] == 1:
                queue.append([i,j]) # 첫 노드 삽입
                graph[i][j] = 0 # 및 방문 처리
                cnt += 1 # queue 한번이 끝나서야 cnt++
                while queue:
                    hidx, widx = queue.popleft() # 노드 꺼냄
                    for d in range(8):
                        nh = hidx + dh[d]
                        nw = widx + dw[d]
                        if 0 <= nh < h and 0 <= nw < w and graph[nh][nw] == 1:
                            queue.append([nh,nw])
                            graph[nh][nw] = 0 # 방문 처리
    print(cnt)

while True:
    w,h = map(int, sys.stdin.readline().rstrip().split()) # 가로, 세로
    if w==0 and h==0: break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution()
