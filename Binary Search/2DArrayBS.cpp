#include<iostream>
#include<vector>
using namespace std;

bool binarySearch2D(vector<vector<int>> matrix, int target) {
    int row = matrix.size();
    int cols = matrix[0].size();
    int start = 0;
    int end = row * cols - 1;
    int mid = start + (end - start) / 2;
    while (start <= end)
    {
        int element = matrix[mid / cols][mid % cols];
        if (element == target) {
            return true;
        }
        if (element < target) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
        mid = start + (end - start) / 2;
    }
    return false;
}
int main(){
    vector<vector<int>> matrix = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    int target = 7;
    if (binarySearch2D(matrix, target)) {
        cout << "Element found" << endl;
    } else {
        cout << "Element not found" << endl;
    }
    return 0;
}
