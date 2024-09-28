import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    field[a][b] = 0

    while q:
        x, y = q.popleft()

        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 정해진 밭 크기를 벗어났을 때
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if field[nx][ny] == 1:
                q.append((nx, ny))
                field[nx][ny] = 0


# T번만큼 반복
T = int(sys.stdin.readline())
for _ in range(T):
    # 배추밭 생성
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0] * N for _ in range(M)]

    # 배추 심기
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        field[a][b] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if field[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)
