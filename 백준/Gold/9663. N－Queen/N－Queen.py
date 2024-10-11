import sys

N = int(sys.stdin.readline())
ans = 0

selected_columns = set()
diagonals1 = set()
diagonals2 = set()


def dfs(row):
    global ans

    if row == N:
        ans += 1
        return

    for column in range(N):
        if column in selected_columns or row - column in diagonals1 or row + column in diagonals2:
            continue

        selected_columns.add(column)
        diagonals1.add(row - column)
        diagonals2.add(row + column)

        dfs(row + 1)

        selected_columns.remove(column)
        diagonals1.remove(row - column)
        diagonals2.remove(row + column)


dfs(0)
print(ans)
