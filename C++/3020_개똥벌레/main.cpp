#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	int n{}, h{};
	cin >> n >> h;

	int arrBarrier1[500001], arrBarrier2[500001];
	for (int i{}; i < n / 2; ++i)
	{
		int temp1{}, temp2{};
		cin >> temp1 >> temp2;

		++arrBarrier1[temp1];
		++arrBarrier2[temp2];
	}

	int arrLine[500001];
	for (int i{}; i < h; ++i)
	{
		if (i == 0 or i == h - 1)
		{
			arrLine[i] = n / 2;
		}
		else
		{
			arrLine[i] = arrLine[i - 1];

			arrLine[i] -= arrBarrier1[i];			
			arrLine[i] += arrBarrier2[h - i];
		}
	}

	sort(arrLine, arrLine + h);
	
	int cnt{};
	for (int i{}; i < h; ++i)
	{
		if (arrLine[i] == arrLine[0])
		{
			++cnt;
		}
		else
		{
			break;
		}
	}

	cout << arrLine[0] << " " << cnt;

	return 0;
}