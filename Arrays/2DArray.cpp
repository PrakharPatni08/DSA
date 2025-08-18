#include<iostream>
#include<climits>
using namespace std;

int rowWiseSum(int arr[][4], int rows, int cols) {
    for(int i = 0; i < rows; i++) {
        int sum = 0;
        for(int j = 0; j < cols; j++) {
            sum += arr[i][j];
        }
        cout << "Sum of row " << i << " is " << sum << endl;
    }
}

bool checkTarget(int arr[][4], int rows, int cols, int target) {
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            if(arr[i][j] == target) {
                return true;
            }
        }
    }
    return false;
}

int largestRowSum(int arr[][4], int rows, int cols) {
    int maxSum = INT_MIN;
    for(int i = 0; i < rows; i++) {
        int sum = 0;
        for(int j = 0; j < cols; j++) {
            sum += arr[i][j];
        }
        maxSum = max(maxSum, sum);
    }
    return maxSum;
}

void printArray(int arr[][4], int rows, int cols) {
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}
int main(){
    int arr[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    int rows = 3;
    int cols = 4;

    cout << "Row-wise sum:" << endl;
    rowWiseSum(arr, rows, cols);

    int target = 7;
    if(checkTarget(arr, rows, cols, target)) {
        cout << "Target " << target << " found in the array." << endl;
    } else {
        cout << "Target " << target << " not found in the array." << endl;
    }

    int largestSum = largestRowSum(arr, rows, cols);
    cout << "Largest row sum is " << largestSum << endl;

    cout << "Array elements are:" << endl;
    printArray(arr, rows, cols);

    return 0;
}
