#백준4963_섬의개수
#DFS

import sys
sys.setrecursionlimit(10000) # 이게 없으면 런타임 에러 발생

def dfs(hidx, widx): # 여기서 h,w를 쓰면 전역변수랑 비교 구문에서 엇갈림
    graph[hidx][widx] = 0 # 방문 처리

    # 북, 북동, 동, 남동, 남, 남서, 서, 북서 방향벡터
    dh = [-1, -1, 0, 1, 1, 1, 0, -1]
    dw = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(8):
        nh = hidx + dh[i]
        nw = widx + dw[i]
        if 0<=nh<h and 0<=nw<w and graph[nh][nw] == 1: # 여기서 엇갈림 발생
            dfs(nh,nw)

def solution():
    cnt = 0
    for i in range(h): # 시작점이 명시되어 있지 않음
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt += 1 # 한번의 dfs 결과가 끝나야만 cnt++
    print(cnt)

while True:
    w,h = map(int, sys.stdin.readline().rstrip().split()) # 가로, 세로
    if w==0 and h==0: break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    solution()
