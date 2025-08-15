#include<iostream>
#include<vector>
using namespace std;
vector<int> reverseArray(vector<int> v) {
    int s = 0;
    int e = v.size() - 1;
    while(s<e) {
        swap(v[s++], v[e--]);
    }
    return v;
}
vector<int> twoArraySum(vector<int>& arr1,int n, vector<int>& arr2, int m) {
    int i = n - 1, j = m - 1;
    vector<int> ans;
    int carry = 0;
    while(i>=0 && j>=0){
        int val1 = arr1[i];
        int val2 = arr2[j];
        int sum = val1 + val2 + carry;
        carry = sum/10;
        sum = sum % 10;
        ans.push_back(sum);
        i--;
        j--;
    }
    //First case arr1 is bigger
    while(i>=0){
        int sum = arr1[i] + carry;
        carry = sum/10;
        sum = sum % 10;
        ans.push_back(sum);
        i--;
    }
    //Second case arr2 is bigger
    while(j>=0){
        int sum = arr2[j] + carry;
        carry = sum/10;
        sum = sum % 10;
        ans.push_back(sum);
        j--;
    }
    //If carry is left
    while(carry!=0){
        int sum = carry;
        carry = sum/10;
        sum = sum % 10;
        ans.push_back(sum);
    }
    //Reverse the answer
    return reverseArray(ans);
}
int main() {
    vector<int> arr1 = {2, 4, 3};
    vector<int> arr2 = {5, 6, 4};
    vector<int> result = twoArraySum(arr1, arr1.size(), arr2, arr2.size());
    for(int i : result) {
        cout << i << " ";
    }
    return 0;
}
