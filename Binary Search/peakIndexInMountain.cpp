#include<iostream>
#include<vector>
using namespace std;
int peakIndexInMountain(vector<int> &arr){
    int s = 0;
    int e = arr.size()-1;
    int m = s + (e-s)/2;
    while(s<e){
        if(arr[m] < arr[m+1]){
            s = m+1;
        }
        else{
            e = m;
        }
        m = s + (e-s)/2;
    }

}
int main(){
    vector<int> arr = {0,2,1,0};
    cout<<peakIndexInMountain(arr);
    return 0;
}