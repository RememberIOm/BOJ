#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main() {
    cin.tie(0); ios_base::sync_with_stdio(false);

    int T; cin >> T;

    while (T--) {
        int k; cin >> k;
        multiset<int> Q;

        while (k--) {
            char input; cin >> input;

            if (input == 'D') {
                int inputNum; cin >> inputNum;

                if (inputNum == -1 && !Q.empty()) {
                    Q.erase(Q.begin());
                }
                else if (inputNum == 1 && !Q.empty()) {
                    Q.erase(--Q.end());
                }
            }
            else {
                int inputNum; cin >> inputNum;
                Q.insert(inputNum);
            }
        }
        
        if (!Q.empty()) {
            cout << *(--Q.end()) << ' ' << *Q.begin() << '\n';
        }
        else {
            cout << "EMPTY\n";
        }
    }
   
    return 0;
}