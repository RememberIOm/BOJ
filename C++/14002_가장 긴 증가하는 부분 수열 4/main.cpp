#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int n{};
    cin >> n;
    
    vector<pair<int, int>> a(n);
    vector<int> checkSizeOnly;
    
    int input{};
    for (int i{}; i < n; ++i) {
        cin >> input;
        a.at(i) = make_pair(input, 0);
    }
    
    checkSizeOnly.push_back(a.front().first);
    
    for (int i{1}; i < n; ++i) {
        if (a.at(i).first > checkSizeOnly.back()) {
            checkSizeOnly.push_back(a.at(i).first);
            a.at(i).second = checkSizeOnly.size() - 1;
        }
        else {
            int checkSizeOnlyIdx{static_cast<int>(lower_bound(checkSizeOnly.begin(), checkSizeOnly.end(), a.at(i).first) - checkSizeOnly.begin())};
            checkSizeOnly.at(checkSizeOnlyIdx) = a.at(i).first;
            a.at(i).second = checkSizeOnlyIdx;
        }
    }
    
    stack<int> checkNumOnly;
    int maxValue{static_cast<int>(checkSizeOnly.size() - 1)};
    for (int i{static_cast<int>(a.size() - 1)}; i >= 0; --i) {
        if (a.at(i).second == maxValue) {
            checkNumOnly.push(a.at(i).first);
            --maxValue;
        }
    }
    
    cout << checkSizeOnly.size() << '\n';
    
    int checkNumOnlySize{static_cast<int>(checkNumOnly.size())};
    for (int i{}; i < checkNumOnlySize; ++i) {
        int output{checkNumOnly.top()};
        cout << output << ' ';
        checkNumOnly.pop();
    }
    
    return 0;
}