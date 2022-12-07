#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int n{};
    cin >> n;
    
    vector<int> a;
    
    int firstInput{};
    cin >> firstInput;
    
    a.push_back(firstInput);
    
    for (int i{1}; i < n; ++i) {
        cin >> firstInput;
        
        if (firstInput > a.back()) {
            a.push_back(firstInput);
        }
        else {
            a.at(lower_bound(a.begin(), a.end(), firstInput) - a.begin()) = firstInput;
        }
    }
    
    cout << a.size();
    
    return 0;
}