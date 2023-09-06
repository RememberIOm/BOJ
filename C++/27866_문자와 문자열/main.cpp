#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    string a; cin >> a;
    int i; cin >> i;
    
    cout << a.at(i - 1);
    
    return 0;
}
