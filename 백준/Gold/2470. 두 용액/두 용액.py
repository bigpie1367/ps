import sys
import math

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

min_diff = math.inf

start_index = 0
end_index = len(li) - 1

while start_index < end_index:
    diff = li[start_index] + li[end_index]
    if abs(diff) < min_diff:
        min_diff = abs(diff)
        result = [li[start_index], li[end_index]]

    if diff > 0:
        end_index -= 1
    else:
        start_index += 1

print(*result)
