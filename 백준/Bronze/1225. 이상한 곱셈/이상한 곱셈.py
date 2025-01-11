a, b = map(list, input().split())

for i in range(len(a)):
    a[i] = int(a[i])

for i in range(len(b)):
    b[i] = int(b[i])

result = sum(a) * sum(b)
print(result)
