import sys
import math

N, S = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))

ans = math.inf
sum = 0
length = 0

start = 0
for end, data in enumerate(li):
    sum += li[end]
    length += 1

    while sum >= S:
        ans = min(ans, length)

        sum -= li[start]
        start += 1
        length -= 1


print(ans if ans != math.inf else 0)
