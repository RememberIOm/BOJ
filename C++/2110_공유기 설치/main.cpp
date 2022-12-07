#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int n{}, c{};
    cin >> n >> c;
    
    vector<int> house(n);
    for (int i{}; i < n; ++i) {
        cin >> house.at(i);
    }
    sort(house.begin(), house.end());
    
    int left{1}, mid{}, right{house.back() - house.front()};
    while (left <= right) {
        mid = (left + right) / 2;
        int apNum{1};
        
        int currentHouse{house.front()};
        for (int i{1}; i < house.size(); ++i) {
            int distance{house.at(i) - currentHouse};
            
            if (distance >= mid) {
                ++apNum;
                currentHouse = house.at(i);
            }
        }
        
        if (apNum >= c) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    
    cout << right;
    
    return 0;
}