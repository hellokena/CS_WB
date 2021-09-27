# 백준2667_단지번호붙이기
cnt = 0
result = []

def solution():
    global cnt
    temp = 0
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))
    for i in range(n): # 시작점 설정 안되어 있으므로 for문
        for j in range(n):
            if graph[i][j] == 1:
                cnt = 0 # 단지 내 집 갯수 초기화
                dfs(i, j, graph, n, temp)
                result.append(cnt)
    print(len(result))
    result.sort()
    for i in result:
        print(i)

def dfs(h, w, graph, n, temp):
    global cnt
    graph[h][w] = 0 # 1. 방문 처리
    cnt += 1 # 단지 내 집 갯수 증가
    # 상하좌우 방향벡터
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if 0<=nh<n and 0<=nw<n and graph[nh][nw] == 1:
            dfs(nh, nw, graph, n, temp)

solution()
