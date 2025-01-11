#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int total_pack_num;
int five_pack;
int third_pack;
int sugar_weight;
int remain_sugar;

int calculate_pack(int sugar_weight)
{
	if (remain_sugar % 3 != 0)
	{
		five_pack--;
		remain_sugar += 5;
		calculate_pack(sugar_weight);

		if (five_pack == -1)
		{
			total_pack_num = -1;
		}
	}
	else
	{
		third_pack = remain_sugar / 3;
		total_pack_num = five_pack + third_pack;
	}

	return total_pack_num;
}

int main(void)
{
	scanf("%d", &sugar_weight);

	five_pack = sugar_weight / 5;
	remain_sugar = sugar_weight % 5;

	total_pack_num = calculate_pack(sugar_weight);

	printf("%d\n", total_pack_num);

	return 0;
}