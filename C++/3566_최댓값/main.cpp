#include <iostream>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    vector<vector<int>> nums(9, vector<int>(9));
    
    for (int col{}; col < 9; ++col) {
        for (int row{}; row < 9; ++row) {
            cin >> nums.at(col).at(row);
        }
    }
    
    int max{}, col_max{1}, row_max{1};
    
    for (int col{}; col < 9; ++col) {
        for (int row{}; row < 9; ++row) {
            if (nums.at(col).at(row) > max) {
                col_max = col + 1;
                row_max = row + 1;
                max = nums.at(col).at(row);
            }
        }
    }
    
    cout << max << "\n" << col_max << " " << row_max;
    
    return 0;
}
