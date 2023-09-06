#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int n; cin >> n;
    
    while (n != -1) {
        vector<int> div{ 1 };
        int sum{ 1 };
        
        for (int i{ 2 }; i <= sqrt(n); ++i) {
            if (n % i) {
                continue;
            }
            
            div.push_back(i);
            div.push_back(n / i);
            
            sum += i + n / i;
        }
        
        if (sum != n) {
            cout << n << " is NOT perfect.\n";
        }
        else {
            sort(div.begin(), div.end());
            
            cout << n << " = ";
            
            for (int i{}; i < div.size(); ++i) {
                cout << div.at(i);
                
                if (i < div.size() - 1) {
                    cout << " + ";
                }
            }
            
            cout << "\n";
        }
        
        cin >> n;
    }
    
    return 0;
}
