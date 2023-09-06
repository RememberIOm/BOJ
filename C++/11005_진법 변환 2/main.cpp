#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int n, b; cin >> n >> b;
    
    int max_pow{};
    
    while (pow(b, max_pow) <= n) {
        ++max_pow;
    }
    
    --max_pow;
    
    vector<int> result_10(max_pow + 1);
    
    for (int i{}; i <= max_pow; ++i) {
        result_10.at(i) = n / pow(b, max_pow - i);
        n %= static_cast<int>(pow(b, max_pow - i));
    }
    
    string result{};
    
    for (auto i : result_10) {
        if (i >= 10) {
            result += 'A' + i - 10;
        }
        else {
            result += to_string(i);
        }
    }
    
    cout << result;
    
    return 0;
}
