import sys


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    x = 0
    x_list = list(map(int, sys.stdin.readline().split()))
    for index, i in enumerate(reversed(x_list)):
        x += i * (10 ** index)

    y = 0
    y_list = list(map(int, sys.stdin.readline().split()))
    for index, i in enumerate(reversed(y_list)):
        y += i * (10 ** index)

    count = 0
    numbers = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        number = 0

        for j in range(M):
            number += numbers[(i + j) % N] * (10 ** (M - j - 1))

        if number >= x and number <= y:
            count += 1

    print(count)