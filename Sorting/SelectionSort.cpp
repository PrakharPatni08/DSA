#include<iostream>
using namespace std;
int selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
            swap(arr[minIndex], arr[i]);
        }
    }

int main() {
    int arr[10] = {64, 25, 12, 22, 11, 90, 45, 78, 34, 23};
    int sorted = selectionSort(arr, 10);
    cout << "Sorted array: \n";
    for (int i = 0; i < 10; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}