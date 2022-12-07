#include <iostream>
using namespace std;

int gcd(const int&, const int&);

int main()
{
	int N{}, M{};
	cin >> N >> M;

	cout << M - gcd(N, M);

	return 0;
}

int gcd(const int& a, const int& b)
{
	if (a % b == 0)
	{
		return b;
	}
	else
	{
		return gcd(b, a % b);
	}
}
