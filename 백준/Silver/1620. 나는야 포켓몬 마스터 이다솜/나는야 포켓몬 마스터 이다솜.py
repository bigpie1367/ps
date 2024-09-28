import sys

N, M = map(int, sys.stdin.readline().split())

name_dict = {}
order_dict = {}

for i in range(N):
    name = sys.stdin.readline().strip()
    name_dict[name] = i
    order_dict[i] = name

for _ in range(M):
    com = sys.stdin.readline().strip()

    if com.isdigit():
        print(order_dict.get(int(com) - 1))
    else:
        print(name_dict[com] + 1)
