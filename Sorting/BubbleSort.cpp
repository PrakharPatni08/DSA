#include<iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
    for (int i = 1; i < n ; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i ; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (swapped == false) break;
    }
}
int main() {
    int arr[10] = {64, 25, 12, 22, 11, 90, 45, 78, 34, 23};
    bubbleSort(arr, 10);
    cout << "Sorted array: \n";
    for (int i = 0; i < 10; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}