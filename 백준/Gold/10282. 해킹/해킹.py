import sys
import math
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    n, d, c = map(int, sys.stdin.readline().split())

    table = [math.inf for _ in range(n)]
    graph = [[] for _ in range(n)]

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b - 1].append((a - 1, s))

    table[c - 1] = 0

    pq = []
    heapq.heappush(pq, (0, c - 1))

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > table[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < table[neighbor]:
                table[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    count = 0
    max_time = 0

    for time in table:
        if time != math.inf:
            count += 1
            max_time = max(max_time, time)

    print(count, max_time)
