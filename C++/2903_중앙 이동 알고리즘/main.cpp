#include <iostream>
#include <cmath>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int n; cin >> n;
    
    cout << static_cast<int>(pow(pow(2, n) + 1, 2));
    
    return 0;
}
