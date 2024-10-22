import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

x = int(sys.stdin.readline())

res = 0
temp = 0

start_index = 0
end_index = len(li) - 1
while start_index < end_index:
    temp = li[start_index] + li[end_index]
    if temp > x:
        end_index -= 1
    elif temp < x:
        start_index += 1
    else:
        start_index += 1
        end_index -= 1

        res += 1

print(res)
