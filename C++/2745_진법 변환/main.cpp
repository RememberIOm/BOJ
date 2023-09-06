#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    string n; int b; cin >> n >> b;
    
    int result{};
    
    for (int i{}; i < n.size(); ++i) {
        char cur_n = n.at(n.size() - i - 1);
        
        if (cur_n <= '9') {
            result += (cur_n - '0') * pow(b, i);
        }
        else {
            result += (cur_n  - 'A' + 10) * pow(b, i);
        }
    }
    
    cout << result;
    
    return 0;
}
