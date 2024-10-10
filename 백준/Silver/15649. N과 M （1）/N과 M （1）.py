import sys

N, M = map(int, sys.stdin.readline().split())

visited = [False] * (N + 1)
ans = []


def dfs(depth):
    global ans

    if depth == M:
        print(*ans)
        return

    for i in range(1, N+1):
        if visited[i]:
            continue

        ans.append(i)
        visited[i] = True

        dfs(depth + 1)

        ans.pop()
        visited[i] = False


dfs(0)
