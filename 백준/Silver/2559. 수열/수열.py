import sys

N, K = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

cur_sum = sum(arr[:K])
max_sum = cur_sum

for i in range(K, N):
    cur_sum = cur_sum + arr[i] - arr[i - K]
    max_sum = max(max_sum, cur_sum)

print(max_sum)
