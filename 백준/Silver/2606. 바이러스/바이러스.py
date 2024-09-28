import sys

N = int(sys.stdin.readline())
L = int(sys.stdin.readline())

# 그래프 생성
graph = [[] for _ in range(N+1)]
for _ in range(L):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)


def dfs():
    # 해당 정점과 연결된 노드들 추가
    if stack:
        node = stack.pop()
        if node not in visited:
            stack.extend(graph[node])
            visited.append(node)
    else:
        return

    dfs()


stack = [1]
visited = []

dfs()

print(len(visited) - 1)
