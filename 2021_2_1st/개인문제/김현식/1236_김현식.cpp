#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>

int main()
{
	int N, M;
	char castle[51][51];
	int blank_row = 0;
	int blank_col = 0;

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++)
			scanf("%s", castle[i]);

	for (int i = 0; i < N; i++)
	{
		int flag = 0;
		for (int j = 0; j < M; j++)
		{
			if (castle[i][j] == 'X')
				flag = 1;
		}
		if (flag == 0)
			blank_row++;
	}

	for (int i = 0; i < M; i++)
	{
		int flag = 0;
		for (int j = 0; j < N; j++)
		{
			if (castle[j][i] == 'X')
				flag = 1;
		}
		if (flag == 0)
			blank_col++;
	}

	if (blank_row > blank_col)
		printf("%d", blank_row);
	else
		printf("%d", blank_col);


	return 0;
}