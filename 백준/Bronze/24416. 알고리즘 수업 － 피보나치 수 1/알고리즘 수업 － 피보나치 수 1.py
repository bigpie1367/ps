import sys


def fib(value):
    if value == 1 or value == 2:
        return 1

    return fib(value - 1) + fib(value - 2)


def fibonacci(value):
    dp = [0] * (value + 1)
    dp[0] = 1
    dp[1] = 1

    cnt = 0
    for i in range(3, value + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        cnt += 1

    return cnt


n = int(sys.stdin.readline())
print(fib(n), fibonacci(n))
