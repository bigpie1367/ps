import sys


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    x = int(''.join(list(sys.stdin.readline().split())))
    y = int(''.join(list(sys.stdin.readline().split())))
    numbers = list(map(int, sys.stdin.readline().split()))

    count = 0
    for i in range(N):
        number = 0

        for j in range(M):
            number += numbers[(i + j) % N] * (10 ** (M - j - 1))

        if number >= x and number <= y:
            count += 1

    print(count)
