#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	string input = "";
	cin >> input;
	int count = 0;
	for (int i = 0; i < input.length(); i++) {
		if (count == 10) {
			cout << endl;
			count = 0;
		}
		cout << input[i];
		count++;
	}
	cout << endl;
	return 0;
}
