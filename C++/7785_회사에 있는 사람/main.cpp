#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int attempt; cin >> attempt;
    
    vector<string> company;
    
    while (attempt--) {
        string name, el; cin >> name >> el;
        
        company.push_back(name);
    }
    
    sort(company.begin(), company.end(), greater<>());
    
    for (int i{}; i < company.size(); ++i) {
        if (i + 1 < company.size() and company.at(i) == company.at(i + 1)) {
            ++i;
        }
        else {
            cout << company.at(i) << "\n";
        }
    }
    
    return 0;
}
