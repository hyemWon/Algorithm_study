#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int n1, int n2) {
	return (n1 > n2) ? true : false;
}

int main()
{
	int N, M;
	cin >> N >> M;
	vector<int>num(N);
	vector<int>result;

	for (int i = 0; i < N; i++) { cin >> num[i]; }
	sort(num.begin(), num.end(), compare);

	for (int i = 0; i < num.size(); i++) {
		for (int j = i + 1; j < num.size(); j++) {
			for (int k = j + 1; k < num.size(); k++) {
				int total = 0;
				total += num[i] + num[j] + num[k];
				if (total <= M) {
					result.push_back(total);
				}
			}
		}
	}
	sort(result.begin(), result.end(), compare);
	cout << result[0] << endl;
	
	return 0;
}
