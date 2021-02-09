//dfs : 시간초과
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int dfs(int layer, int n) {
	int answer = 0;
	if (layer == 1) { return n; }
	else {
		for (int i = 1; i <= n; i++) {
			answer += dfs(layer - 1, i);
		}
		return answer;
	}
}

int main()
{
	int T;
	cin >> T;
	for (int cnt = 0; cnt < T; cnt++) {
		int N, M;
		cin >> N >> M;
		cout << dfs(N, M - N + 1) << endl;
	}
	
	return 0;
}

//조합성질 : n+1Cr = nCr + nCr-1 (시간초과)
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int dp(int n, int m) {
	if (n == m) return 1;
	else if (n == 1) return m;
	else return dp(n - 1, m - 1) + dp(n, m - 1);
}

int main() {
	int t;
	cin >> t;
	while (t--) {
		int n, m;
		cin >> n >> m;
		cout << dp(n, m);
	}
	return 0;
}
