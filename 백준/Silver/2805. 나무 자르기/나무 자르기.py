import sys

N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))


def binary_search(arr, start, end, target):
    if start > end:
        return 0

    mid = (start + end) // 2

    length = 0
    for data in arr:
        if data > mid:
            length += data - mid

    if length >= target:
        return max(mid, binary_search(arr, mid+1, end, target))
    elif length < target:
        return binary_search(arr, start, mid-1, target)


print(binary_search(trees, 1, max(trees), M))
