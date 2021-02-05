#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

vector<int> point[1001];
int N, M, start;
bool dfs_check[1001];
bool bfs_check[1001];

void dfs(int index)
{
	dfs_check[index] = true;
	cout << index << " ";

	for (int i = 0; i < point[index].size(); i++)
	{
		if (!dfs_check[point[index][i]])
			dfs(point[index][i]);
	}

}

void bfs(int index)
{
	queue<int> q;
	
	bfs_check[index] = true;
	q.push(index);

	while (!q.empty())
	{
		int num = q.front();
		cout << num << " ";
		q.pop();

		for (int i = 0; i < point[num].size(); i++)
		{
			if (!bfs_check[point[num][i]])
			{
				q.push(point[num][i]);
				bfs_check[point[num][i]] = true;
			}
		}

	}


}

int main(void)
{
	cin >> N >> M >> start;

	for (int i = 0; i < M; i++)
	{
		int num1, num2;
		cin >> num1 >> num2;
		point[num1].push_back(num2);
		point[num2].push_back(num1);
	}

	for (int i = 0; i < N; i++)
		sort(point[i].begin(), point[i].end());


	dfs(start);
	printf("\n");
	bfs(start);

	return 0;
}