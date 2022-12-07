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

    int M, N, H; cin >> M >> N >> H;

    vector<vector<vector<Tomato>>> vec;
    queue<vector<int>> queue;

    for (int i{}; i < H; ++i) {
        vector<vector<Tomato>> vecCol;

        for (int j{}; j < N; ++j) {
            vector<Tomato> vecRow;

            for (int k{}; k < M; ++k) {
                int input; cin >> input;
                vecRow.push_back(Tomato(input));

                if (input == 1) {
                    vector<int> idx = { k, j, i };
                    queue.push(idx);
                }
            }

            vecCol.push_back(vecRow);
        }

        vec.push_back(vecCol);
    }

    int day{ 1 };

    for (int isChanged{ 1 }; isChanged == 1; ++day) {
        isChanged = 0;

        auto curQueueSize{ queue.size() };
        const vector<int> sumX = { 0, -1, 0, 1, 0, 0 };
        const vector<int> sumY = { -1, 0, 1, 0, 0, 0 };
        const vector<int> sumZ = { 0, 0, 0, 0, 1, -1 };

        while (curQueueSize--) {
            vector<int> curVec{ queue.front() };
            queue.pop();

            for (int sumNum{}; sumNum < sumX.size(); ++sumNum) {
                int idxX{ curVec.at(0) + sumX.at(sumNum) };
                int idxY{ curVec.at(1) + sumY.at(sumNum) };
                int idxZ{ curVec.at(2) + sumZ.at(sumNum) };

                try {
                    if (vec.at(idxZ).at(idxY).at(idxX).state == 0) {
                        vec.at(idxZ).at(idxY).at(idxX).state = day + 1;
                        vector<int> idxVec = { idxX, idxY, idxZ };
                        queue.push(idxVec);
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
            for (auto k : j) {
                if (k.state == 0) isComplete = false;
            }
        }
    }

    if (isComplete)
        cout << day - 2;
    else
        cout << -1;

    return 0;
}