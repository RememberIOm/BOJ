#include <iostream>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int64_t n; cin >> n;
    
    cout << n * (n - 1) * (n - 2) / 6 << "\n3";
    
    return 0;
}
