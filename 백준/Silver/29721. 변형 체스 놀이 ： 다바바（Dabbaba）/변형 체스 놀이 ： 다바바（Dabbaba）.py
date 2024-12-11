import sys

dx = [0, -2, 2, 0]
dy = [-2, 0, 0, 2]

visited = set()
babas = []

count = 0

N, K = map(int, sys.stdin.readline().split())
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    babas.append((x - 1, y - 1))
    visited.add((x - 1, y - 1))

for x, y in babas:
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > (N - 1) or ny > (N - 1):
            continue

        if (nx, ny) not in visited:
            visited.add((nx, ny))
            count += 1

print(count)
