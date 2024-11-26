import math
from sys import stdin


N, M = map(int, stdin.readline().split())
min_package, min_piece = math.inf, math.inf

for _ in range(M):
    package, piece = map(int, stdin.readline().split())
    min_package = min(min_package, package)
    min_piece = min(min_piece, piece)

package_value = math.ceil(N / 6) * min_package
print(min(package_value, (N // 6) * min_package + (N % 6) * min_piece, N * min_piece))
