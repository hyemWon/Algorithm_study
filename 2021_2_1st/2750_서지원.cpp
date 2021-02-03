#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int N;
	vector<int> num;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		num.push_back(temp);
	}
	sort(num.begin(), num.end());
	for (int i = 0; i < N; i++) {
		cout << num[i] << endl;
	}
	return 0;
}
