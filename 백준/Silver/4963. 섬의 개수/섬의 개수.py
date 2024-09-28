import sys
from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(i, j):
    q = deque()
    q.append((i, j))

    graph[i][j] = 0

    while q:
        y, x = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((ny, nx))


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    # 지도 생성
    graph = [[0] * w for _ in range(h)]
    for i in range(h):
        graph[i] = list(map(int, sys.stdin.readline().split()))

    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                count += 1
                bfs(i, j)

    print(count)
