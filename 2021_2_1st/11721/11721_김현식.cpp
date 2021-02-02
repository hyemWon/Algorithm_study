#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<iostream>
#include<cstring>

char input[101];

int main()
{
	scanf("%s", input);

	for (int i = 0; i < strlen(input); i++)
	{
		printf("%c", input[i]);
		if (i % 10 == 9)
			printf("\n");
	}


	return 0;
}