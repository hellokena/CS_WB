#백준7562_나이트의이동

import sys
from collections import deque

def solution(starth, startw, goalh, goalw):
    queue = deque()
    queue.append([starth, startw]) # 시작 노드 삽입
    #시작 위치는 이 까지 가기 위해서 거리가 0이므로 처리 하지 않음
    #graph[starth][startw] = 1 # graph 좌표마다 각 그 자리 가기 위한 거리 계산
    while queue:
        hidx, widx = queue.popleft()
        # 처음에 탐색 완료하면 그때까지가 최소
        if hidx == goalh and widx == goalw: break
        # 시계방향 방향벡터
        dh = [2, 1, -1, -2, -2, -1, 1, 2]
        dw = [1, 2, 2, 1, -1, -2, -2, -1]
        for d in range(8):
            nh = hidx + dh[d]
            nw = widx + dw[d]
            if 0<=nh<l and 0<=nw<l and graph[nh][nw]==0: # 방문하지 않았으면
                queue.append([nh,nw])
                graph[nh][nw] = graph[hidx][widx] + 1
    print(graph[goalh][goalw])

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    l = int(sys.stdin.readline().rstrip()) # 변의 길이
    graph = [[0]*l for _ in range(l)]
    starth, startw = map(int, sys.stdin.readline().rstrip().split())
    goalh, goalw = map(int, sys.stdin.readline().rstrip().split())
    solution(starth, startw, goalh, goalw)
