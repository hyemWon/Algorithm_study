#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	vector<string>days(7);
	vector<int>months(12);
	days = { "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN" };
	months = { 31,28,31,30,31,30,31,31,30,31,30,31 };
	int x, y;
	cin >> x >> y;
	int day = 0;
	for (int i = 0; i < x - 1; i++)
		day += months[i];
	day += y;
	int result = day % 7 - 1;
	if (result == -1) { result = 6; }
	cout << days[result] << endl;
	return 0;
}
