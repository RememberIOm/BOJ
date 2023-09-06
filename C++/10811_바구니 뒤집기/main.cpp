#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int box_num, attempt; cin >> box_num >> attempt;
    
    vector<int> boxes(box_num);
    for (int i{}; i < box_num; ++i) {
        boxes.at(i) = i + 1;
    }
    
    for (int i{}; i < attempt; ++i) {
        int a, b; cin >> a >> b;
        
        reverse(boxes.begin() + a - 1, boxes.begin() + b);
    }
    
    for (int i{}; i < box_num; ++i) {
        cout << boxes.at(i) << " ";
    }
    
    return 0;
}
