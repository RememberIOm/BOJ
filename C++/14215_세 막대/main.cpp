#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int a, b, c; cin >> a >> b >> c;
    
    vector<int> tri{ a, b, c };
    
    sort(tri.begin(), tri.end());
    
    if (tri.at(0) + tri.at(1) > tri.at(2)) {
        cout << a + b + c;
    }
    else {
        cout << (tri.at(0) + tri.at(1)) * 2 - 1;
    }
            
    return 0;
}
