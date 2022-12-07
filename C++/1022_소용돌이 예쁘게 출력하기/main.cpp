#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <climits>
using namespace std;

int get(int r, int c);
int up(int r, int c);
int left(int r, int c);
int down(int r, int c);
int right(int r, int c);

int main()
{
	int r1, c1, r2, c2;
	cin >> r1 >> c1 >> r2 >> c2;

	int max{ INT_MIN };
	for (int r{ r1 }; r <= r2; ++r)
	{
		for (int c{ c1 }; c <= c2; ++c)
		{
			int num{ get(r, c) };
			if (num > max)
			{
				max = num;
			}
		}
	}

	string strNum{ to_string(max) };

	for (int r{ r1 }; r <= r2; ++r)
	{
		for (int c{ c1 }; c <= c2; ++c)
		{
			cout << setw( strNum.length() )
				<< get(r, c) << " ";
		}

		cout << "\n";
	}

	return 0;
}

int get(int r, int c)
{
	int result{};

	if (c >= 0 and abs(r) <= c)
	{
		result = up(r, c);
	}
	else if (r < 0 and abs(c) < -r)
	{
		result = left(r, c);
	}
	else if (c < 0 and abs(r) <= -c)
	{
		result = down(r, c);
	}
	else
	{
		result = right(r, c);
	}

	return result;
}

int up(int r, int c)
{
	int key{ 2 * c + 1 };

	if (r == c)
	{
		return key * key;
	}
	else
	{
		return up(c - 1, c - 1) + (c - r);
	}
}

int left(int r, int c)
{
	int key{ up(r, r * -1) };

	return key - (r + c);
}

int down(int r, int c)
{
	int key{ left(c, c) };

	return key - (c - r);
}

int right(int r, int c)
{
	int key{ down(r, r * -1) };

	return key + (r + c);
}