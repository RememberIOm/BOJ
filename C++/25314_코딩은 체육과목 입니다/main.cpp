#include <iostream>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int n; cin >> n;
    
    for (int i{}; i < n / 4; ++i) {
        cout << "long ";
    }
    
    cout << "int";
    
    return 0;
}
