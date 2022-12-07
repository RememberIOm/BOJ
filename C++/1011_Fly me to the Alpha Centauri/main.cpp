#include <iostream>
#include <cmath>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int t{};
    cin >> t;
    
    for (int i{}; i < t; ++i) {
        long long x{}, y{};
        cin >> x >> y;
        long long distance{y - x};
        
        long long sqrtDistance{static_cast<long long>(sqrt(distance))};
        
        if (sqrtDistance * sqrtDistance == distance) {
            cout << sqrtDistance * 2 - 1 << '\n';
        }
        else if (distance <= static_cast<long long>(((sqrtDistance + 1) * (sqrtDistance + 1) + sqrtDistance * sqrtDistance) / 2)) {
            cout << sqrtDistance * 2 << '\n';
        }
        else {
            cout << sqrtDistance * 2 + 1 << '\n';
        }
    }
    
    return 0;
}