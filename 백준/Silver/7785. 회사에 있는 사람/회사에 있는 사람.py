n = int(input())

log = set()

for _ in range(n):
    name, action = input().split()

    if action == 'enter':
        log.add(name)

    elif action == 'leave':
        log.remove(name)

log = list(log)
log.sort(reverse=True)
for data in log:
    print(data)
