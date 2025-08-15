#include<iostream>
#include<vector>
using namespace std;
void rotateArray(vector<int>& arr, int k) {
    vector<int> temp(arr.size());
    for (int i = 0; i < arr.size(); i++) {
        temp[(i + k) % arr.size()] = arr[i];//cyclic shift by k places
    }
    arr = temp;
}
int main(){
    vector<int> arr = {1, 2, 3, 4, 5};
    int k = 4;
    rotateArray(arr, k);
    for (int i : arr) {
        cout << i << " ";
    }
    return 0;
}