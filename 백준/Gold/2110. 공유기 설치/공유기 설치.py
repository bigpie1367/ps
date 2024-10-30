import sys

N, K = map(int, sys.stdin.readline().split())

arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()


def binary_search(arr, start, end, target):
    if start > end:
        return 0

    mid = (start + end) // 2

    count = 1
    current = arr[0]

    for data in arr:
        if data - current >= mid:
            count += 1

            current = data

    if count >= target:
        return max(mid, binary_search(arr, mid + 1, end, target))
    else:
        return binary_search(arr, start, mid - 1, target)


start = 1
end = arr[-1] - arr[0]

print(binary_search(arr, start, end, K))
