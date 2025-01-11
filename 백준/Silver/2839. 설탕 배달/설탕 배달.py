sugar = int(input())

flag = False

bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        flag = True

        bag += (sugar // 5)
        print(bag)
        break

    sugar -= 3
    bag += 1

if flag is False:
    print(-1)
