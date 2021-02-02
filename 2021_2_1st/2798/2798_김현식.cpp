#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>

int M;
int N;

int main()
{
	scanf("%d %d", &N, &M);

	int* num = new int[N];

	for (int i = 0; i < N; i++)
		scanf("%d", &num[i]);

	int max = 0;

	for (int i = 0; i < (N - 2); i++)
	{
		for (int j = i + 1; j < (N - 1); j++)
		{
			for (int k = j + 1; k < N; k++)
			{
				int sum = 0;
				sum = num[i] + num[j] + num[k];
				if ((sum <= M) && (sum > max))
					max = sum;
			}
		}
	}
	printf("%d", max);

	return 0;
}