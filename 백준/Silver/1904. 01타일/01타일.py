import sys


def dp(value): 
    table = [0] * (value + 1)
    table[0] = 1
    table[1] = 2

    for i in range(2, value):
        table[i] = (table[i - 1] + table[i - 2]) % 15746

    return table[value - 1]


n = int(sys.stdin.readline())
print(dp(n))
