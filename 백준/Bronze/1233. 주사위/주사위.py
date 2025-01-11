s1, s2, s3 = map(int, input().split())

li = []

for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            li.append(i + j + k)

result = 0
max_count = 0
max_value = max(li)
for value in range(1, max_value + 1):
    count = li.count(value)
    if count > max_count:
        max_count = count
        result = value

print(result)
