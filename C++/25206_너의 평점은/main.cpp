#include <iostream>
#include <vector>
#include <map>
#include <numeric>
using namespace std;

int main() {
    cin.tie(NULL); ios_base::sync_with_stdio(false);
    
    map<string, double> grade_to_score{
        {"A+", 4.5},
        {"A0", 4.0},
        {"B+", 3.5},
        {"B0", 3.0},
        {"C+", 2.5},
        {"C0", 2.0},
        {"D+", 1.5},
        {"D0", 1.0},
        {"F", 0.0}
    };
    vector<double> grades{};
    int credit_sum{};
    
    for (int i{}; i < 20; ++i) {
        string name, grade; double credit;
        cin >> name >> credit >> grade;
        
        if (grade == "P") {
            continue;
        }
        
        grades.push_back(credit * grade_to_score.at(grade));
        credit_sum += credit;
    }
    
    cout << accumulate(grades.begin(), grades.end(), 0.0) / credit_sum;
    
    return 0;
}
