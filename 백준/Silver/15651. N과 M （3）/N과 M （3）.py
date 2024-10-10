import sys

N, M = map(int, sys.stdin.readline().split())

ans = []


def dfs(depth):
    global ans

    if depth == M:
        print(*ans)
        return

    for i in range(1, N+1):
        ans.append(i)

        dfs(depth + 1)

        ans.pop()


dfs(0)
