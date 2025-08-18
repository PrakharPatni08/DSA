#include<iostream>
#include<vector>
using namespace std;

vector<int> wavePrint(int arr[][4], int rows, int cols) {
    vector<int> ans;
    for(int j = 0; j < cols; j++) {
        if(j % 2 == 0) {
            // Even column: top to bottom
            for(int i = 0; i < rows; i++) {
                ans.push_back(arr[i][j]);
            }
        } else {
            // Odd column: bottom to top
            for(int i = rows - 1; i >= 0; i--) {
                ans.push_back(arr[i][j]);
            }
        }
    }
    return ans;
}

void printVector(const vector<int>& arr) {
    for(int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    int rows = 3;
    int cols = 4;

    vector<int> wave = wavePrint(arr, rows, cols);
    cout << "Wave Print: ";
    printVector(wave);

    return 0;
}