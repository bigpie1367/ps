import sys
import math
import heapq

N, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N)]
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())

    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))


def dijkstra(start):
    start -= 1

    table = [math.inf for _ in range(N)]
    table[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > table[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = weight + table[current_node]

            if distance < table[neighbor]:
                table[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return table


n1, n2 = map(int, sys.stdin.readline().split())

start_table = dijkstra(1)
n1_table = dijkstra(n1)
n2_table = dijkstra(n2)

n1_distance = start_table[n1 - 1] + n1_table[n2 - 1] + n2_table[N - 1]
n2_distance = start_table[n2 - 1] + n2_table[n1 - 1] + n1_table[N - 1]

if n1_distance == math.inf and n2_distance == math.inf:
    print("-1")
else:
    print(min(n1_distance, n2_distance))
