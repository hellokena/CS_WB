# 최단 경로는 bfs
from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0]) # 무방향 그래프
    visited = [0]*(n+1)

    q = deque([(1,0)]) # 1. 처음 노드 큐 삽입 + 길이
    visited[1] = 1 # 1번 시작 노드는 우선 방문 처리
    dist_list= []
    while q:
        tmp, dist = q.popleft()
        for n in graph[tmp]:
            if visited[n] == 0:
                visited[n] = 1
                q.append((n, dist+1))
                dist_list.append(dist+1)
    answer = dist_list.count(max(dist_list))
    return answer
