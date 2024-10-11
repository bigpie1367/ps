import sys
import math
import heapq


V, E = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline())

table = [math.inf for _ in range(V)]
graph = [[] for _ in range(V)]
visited = [False] * V

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())

    graph[u - 1].append((v-1, w))
table[start - 1] = 0

pq = []
heapq.heappush(pq, (0, start - 1))

while pq:
    current_dist, current_node = heapq.heappop(pq)

    if current_dist > table[current_node]:
        continue

    for neighbor, weight in graph[current_node]:
        distance = current_dist + weight

        if distance < table[neighbor]:
            table[neighbor] = distance
            heapq.heappush(pq, (distance, neighbor))


for weight in table:
    if weight == math.inf:
        print('INF')
    else:
        print(weight)
