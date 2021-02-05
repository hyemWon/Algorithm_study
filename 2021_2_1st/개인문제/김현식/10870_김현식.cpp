#include<iostream>

using namespace std;

int input;

int fibo(int num)
{
	int answer = 0;

	if (num == 0)
		return 0;
	if (num == 1)
		return 1;

	answer = fibo(num - 1) + fibo(num - 2);

	return answer;
}

int main(void)
{
	cin >> input;

	cout << fibo(input);

	return 0;
}