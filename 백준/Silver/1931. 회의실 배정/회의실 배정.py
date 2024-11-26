import sys

time_table = []


N = int(sys.stdin.readline())
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    time_table.append((start, end))

time_table = sorted(time_table, key=lambda x: (x[1], x[0]))

count = 0
end_time = 0
for start, end in time_table:
    if start >= end_time:
        end_time = end
        count += 1

print(count)
