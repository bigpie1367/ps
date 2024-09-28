import sys

N = int(input())
input_line_1 = list(map(int, sys.stdin.readline().split()))

M = int(input())
input_line_2 = list(map(int, sys.stdin.readline().split()))

card_dict = {}
for data in input_line_1:
    if data not in card_dict.keys():
        card_dict[data] = 1
    else:
        card_dict[data] = card_dict.get(data) + 1

for data in input_line_2:
    if data in card_dict:
        print(card_dict.get(data), end=" ")
    else:
        print(0, end=" ")
