import sys

K, N = map(int, sys.stdin.readline().split())

lens = []
for _ in range(K):
    lens.append(int(sys.stdin.readline()))

max_len = max(lens)


def binary_search(arr, start, end, target):
    if start > end:
        return 0

    mid = (start + end) // 2

    count = 0
    for data in arr:
        count += data // mid

    if count >= target:
        return max(mid, binary_search(arr, mid + 1, end, target))
    elif count < target:
        return binary_search(arr, start, mid - 1, target)

    return 0


print(binary_search(lens, 1, max_len, N))
