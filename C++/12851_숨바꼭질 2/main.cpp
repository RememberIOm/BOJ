#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);

    int N, K; cin >> N >> K;

    queue<pair<int, int>> Q;
    Q.push(make_pair(N, 0));
    vector<int> visited(100001);
    visited.at(N) = 1;

    int sec{}, routeNum{};

    for (; !Q.empty(); ) {
        int curN{ Q.front().first };
        int curSec{ Q.front().second };
        Q.pop();

        visited.at(curN) = 1;

        if (curN == K and sec == 0) {
            sec = curSec;
            ++routeNum;
        }
        else if (curN == K and sec == curSec) {
            ++routeNum;
        }

        for (int i : {2 * curN, curN + 1, curN - 1}) {
            if (i >= 0 and i <= 100000 and visited.at(i) == 0) {
                Q.push(make_pair(i, curSec + 1));
            }
        }
    }

    cout << sec << '\n' << routeNum;

    return 0;
}