import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

visited = [False] * N
ans = 0


def dfs(n, weight):
    global ans

    if weight < 500:
        return

    if n == N:
        ans += 1
        return

    weight -= K

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        dfs(n + 1, weight + arr[i])
        visited[i] = False


dfs(0, 500)
print(ans)
