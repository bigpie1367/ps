import sys

N = int(sys.stdin.readline())
n_li = list(map(int, sys.stdin.readline().split()))
n_li.sort()

M = int(sys.stdin.readline())
m_li = list(map(int, sys.stdin.readline().split()))


def binary_search(arr, start, end, target):
    if start > end:
        return 0

    mid = (start + end) // 2

    value = arr[mid]
    if target == value:
        return 1
    elif target > value:
        return binary_search(arr, mid + 1, end, target)
    elif target < value:
        return binary_search(arr, start, mid - 1, target)


for data in m_li:
    print(binary_search(n_li, 0, N-1, data))
