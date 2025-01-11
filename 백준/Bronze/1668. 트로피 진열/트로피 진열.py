li = []

N = int(input())
for _ in range(N):
    li.append(int(input()))

count = 0
max_value = 0

for _ in range(2):
    count = 0
    max_value = 0

    for value in li:
        if value > max_value:
            max_value = value
            count += 1

    print(count)
    li.reverse()
