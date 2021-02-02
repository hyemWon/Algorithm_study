#include<cstdio>
#include<iostream>

int mon;
int day;

int main()
{
	scanf_s("%d %d", &mon, &day);

	int gap = 0;
	
	for (int i = 1; i < mon; i++)
	{
		if ((i == 1) || (i == 3) || (i == 5) || (i == 7) || (i == 8) || (i == 10) || (i == 12))
			gap = gap + 31;
		if ((i == 4) || (i == 6) || (i == 9) || (i == 11))
			gap = gap + 30;
		if (i == 2)
			gap = gap + 28;
	}
	gap = gap + day;
	gap = gap % 7;

	if (gap == 0)
		printf("SUN");
	if (gap == 1)
		printf("MON");
	if (gap == 2)
		printf("TUE");
	if (gap == 3)
		printf("WED");
	if (gap == 4)
		printf("THU");
	if (gap == 5)
		printf("FRI");
	if (gap == 6)
		printf("SAT");

	return 0;
}