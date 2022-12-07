#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	cin.tie(NULL); ios_base::sync_with_stdio(false);

	int n{}, k{};
	cin >> n >> k;

	int first{}, mid{}, last{ k };
	while (first < last) {
		mid = (first + last) / 2;
		long long make{};

		for (int i{}; i < n; ++i) {
			make += min(mid / (i + 1), n);
		}

		if (k > make) {
			first = mid + 1;
		}
		else {
			last = mid;
		}
	}

	cout << last;

	return 0;
}