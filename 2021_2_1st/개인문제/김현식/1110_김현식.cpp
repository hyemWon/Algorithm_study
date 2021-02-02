#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>

int input;
int num;

int plus_cycle()
{
	int first, second;
	int new_num;

	first = num / 10;
	second = num % 10;
	new_num = first + second;

	new_num = second * 10 + new_num % 10;

	return new_num;
}

int main()
{
	scanf("%d", &input);
	num = input;
	int answer = 0;

	num = plus_cycle();
	answer++;
	while (num != input)
	{
		num = plus_cycle();
		answer++;
	}

	printf("%d", answer);

	return 0;
}