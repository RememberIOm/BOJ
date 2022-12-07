#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Tomato {
public:
    int state{ -1 };

    Tomato(const int& input) { state = input; }
};

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);

    int M, N; cin >> M >> N;

    vector<vector<Tomato>> vec;
    queue<pair<int, int>> queue;

    for (int i{}; i < N; ++i) {
        vector<Tomato> vecRaw;

        for (int j{}; j < M; ++j) {
            int input; cin >> input;
            vecRaw.push_back(Tomato(input));
            if (input == 1) {
                queue.push(pair<int, int>(j, i));
            }
        }

        vec.push_back(vecRaw);
    }

    int day{ 1 };

    for (int isChanged{ 1 }; isChanged == 1; ++day) {
        isChanged = 0;

        auto curQueueSize{ queue.size() };
        vector<int> sumX = { 0, -1, 0, 1 };
        vector<int> sumY = { -1, 0, 1, 0 };

        while (curQueueSize--) {
            pair<int, int> curPair{ queue.front() };
            queue.pop();

            for (int sumNum{}; sumNum < 4; ++sumNum) {
                int idxX{ curPair.first + sumX.at(sumNum) };
                int idxY{ curPair.second + sumY.at(sumNum) };

                try {
                    if (vec.at(idxY).at(idxX).state == 0) {
                        vec.at(idxY).at(idxX).state = day + 1;
                        queue.push(pair<int, int>(idxX, idxY));
                        isChanged = 1;
                    }
                }
                catch(const std::exception& e) {}
            }
        }
    }

    bool isComplete{ true };

    for (auto i : vec) {
        for (auto j : i) {
            if (j.state == 0) isComplete = false;
        }
    }

    if (isComplete)
        cout << day - 2;
    else
        cout << -1;

    return 0;
}