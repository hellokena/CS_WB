# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# BFS
from collections import deque

n = int(input()) # 크기
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

# 상하좌우 방향벡터
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def dfs(h,w):
	queue = deque([(h,w)]) # 1. 삽입
	while queue:
		nowh, noww = queue.popleft()
		for i in range(4):
			nexth = nowh + dh[i]
			nextw = noww + dw[i]
			if 0<=nexth<n and 0<=nextw<n and graph[nexth][nextw] == 1:
				graph[nexth][nextw] = graph[nowh][noww] + 1 # 방문처리
				queue.append([nexth, nextw]) # 삽입
	print(graph[-1][-1])

dfs(0,0)
