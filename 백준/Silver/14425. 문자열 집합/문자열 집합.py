import sys

N, M = map(int, sys.stdin.readline().split())

result = 0
res_set = set()

for _ in range(N):
    res_set.add(sys.stdin.readline())

for _ in range(M):
    input_text = sys.stdin.readline()

    if input_text in res_set:
        result += 1

print(result)
