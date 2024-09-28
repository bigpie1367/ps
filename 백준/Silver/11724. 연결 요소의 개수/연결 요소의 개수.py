import sys
sys.setrecursionlimit(100000)


def dfs(v):
    if v in nodes:
        nodes.remove(v)

        linked_nodes = graph[v]
        for node in linked_nodes:
            if node in nodes:
                dfs(node)


N, M = map(int, sys.stdin.readline().split())

# 그래프 생성
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0

nodes = [i+1 for i in range(N)]
while nodes:
    count += 1
    dfs(nodes[0])

print(count)
