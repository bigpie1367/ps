import sys


def dp(value):
    if value < 5:
        table = [0] * 5
    else:
        table = [0] * value

    table[0] = 1
    table[1] = 1
    table[2] = 1
    table[3] = 2
    table[4] = 2

    for i in range(5, value):
        table[i] = table[i - 1] + table[i - 5]

    return table[value - 1]


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp(n))
