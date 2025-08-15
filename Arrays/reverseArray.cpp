#include<iostream>
#include<vector>
using namespace std;
int reverseArray(vector<int>& arr) {
    int start = 0;
    int end = arr.size()-1;
    while(start<end){
        swap(arr[start], arr[end]);
        start++;
        end--;
    }
    return 0;
}
void printVector(const vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}
int main(){
    vector<int> arr = {1, 2, 3, 4, 5};
    cout << "Original array: ";
    printVector(arr);
    reverseArray(arr);
    cout << "Reversed array: ";
    printVector(arr);
    return 0;
}