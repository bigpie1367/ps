X = input()
Y = X

temp = 0
count = 0
while True:
    for value in Y:
        temp += int(value)

    if len(Y) == 1:
        print(count)
        if temp % 3 == 0:
            print('YES')
        else:
            print('NO')

        break

    Y = str(temp)
    temp = 0
    count += 1
