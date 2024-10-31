import sys
import copy

S = sys.stdin.readline().strip()
q = int(sys.stdin.readline())

arr = [[0] * 26 for _ in range(len(S))]

for index, char in enumerate(S):
    if index == 0:
        arr[index][ord(char) - 97] += 1
    else:
        arr[index] = copy.deepcopy(arr[index - 1])
        arr[index][ord(char) - 97] += 1

for _ in range(q):
    line = sys.stdin.readline().split()

    target = line[0]
    start = int(line[1])
    end = int(line[2])

    if start == 0:
        print(arr[end][ord(target) - 97])
    else:
        print(arr[end][ord(target) - 97] - arr[start - 1][ord(target) - 97])
