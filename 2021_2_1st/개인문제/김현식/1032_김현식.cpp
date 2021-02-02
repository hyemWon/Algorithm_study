#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstring>

int main()
{
	int num;
	char name[50][51];
	char answer[51] = "";

	scanf("%d", &num);
	for (int i = 0; i < num; i++)
		scanf("%s", name[i]);
	
	for (int i = 0; i < strlen(name[0]); i++)
	{
		int flag = 0;
		char temp = name[0][i];
		for (int j = 1; j < num; j++)
		{
			if (temp != name[j][i])
				flag = 1;
			temp = name[j][i];
		}
		if (flag == 1)
			answer[i] = '?';
		else
			answer[i] = name[0][i];
	}

	printf("%s", answer);
	return 0;
}