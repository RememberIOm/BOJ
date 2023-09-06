#include <iostream>
#include <vector>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    int box_num, attempt; cin >> box_num >> attempt;
    
    vector<int> boxes(box_num);
    
    for (int i{}; i < attempt; ++i) {
        int start, end, ball; cin >> start >> end >> ball;
        
        for (int j{ start }; j <= end; ++j) {
            boxes.at(j - 1) = ball;
        }
    }
    
    for (int i{}; i < box_num; ++i) {
        cout << boxes.at(i) << " ";
    }
    
    return 0;
}
