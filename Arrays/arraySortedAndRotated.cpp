#include<iostream>
#include<vector>
using namespace std;
bool check(vector<int>& arr) {
    int n = arr.size();
    int count = 0;
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i - 1]) {
            count++;
        }
    }
    if(arr[n-1] > arr[0]){
        count++;
    }
    return count <= 1;
}
int main(){
    vector<int> arr = {1,1,1,1,1};
    if (check(arr)) {
        cout << "Array is sorted and rotated." << endl;
    } else {
        cout << "Array is not sorted and rotated." << endl;
    }
    return 0;
}