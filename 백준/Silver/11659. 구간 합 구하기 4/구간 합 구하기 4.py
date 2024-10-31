import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

for i in range(1, len(arr)):
    arr[i] = arr[i] + arr[i - 1]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())

    if start == 1:
        print(arr[end - 1])
    else:
        print(arr[end - 1] - arr[start - 2])
