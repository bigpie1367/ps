value = int(input())
temp_value = value

while True:
    flag = True

    for i in str(temp_value):
        if i != '4' and i != '7':
            temp_value -= 1
            flag = False

            break

    if flag:
        print(temp_value)
        break
