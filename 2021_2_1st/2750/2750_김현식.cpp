#define CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<iostream>

int input = 0;
int num[1000];


int main()
{
	scanf_s("%d", &input);
	for (int i = 0; i < input; i++)
		scanf_s("%d", &num[i]);

	for (int i = 0; i < (input-1); i++)
	{
		for (int j = (i+1); j < input; j++)
		{
			if (num[i] > num[j])
			{
				int temp = num[i];
				num[i] = num[j];
				num[j] = temp;
			}
		}
	}
	for (int i = 0; i < input; i++) {
		printf("%d", num[i]);
		if (i != input - 1)
			printf("\n");
	}
		

	return 0;
}