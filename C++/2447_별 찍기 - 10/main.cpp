#include <iostream>
using namespace std;

bool isStar(const int& x, const int& y, const int& entire) {
	if (x >= entire / 3 and x < entire / 3 * 2 and y >= entire / 3 and y < entire / 3 * 2) {
		return false;
	}
	else {
		if (entire == 3) {
			return true;
		}
		else {
			return isStar(x % (entire / 3), y % (entire / 3), entire / 3);
		}
	}
}

int main() {
	cin.tie(NULL); ios_base::sync_with_stdio(false);

	int N; cin >> N;

	for (int col{}; col < N; ++col) {
		for (int row{}; row < N; ++row) {
			if (isStar(row, col, N)) {
				cout << '*';
			}
			else {
				cout << ' ';
			}
		}

		cout << '\n';
	}

	return 0;
}