#include<iostream>
using namespace std;
int binarySearch(int arr[], int size, int key){
    int start = 0;
    int end = size - 1;
    int mid = start + (end - start) / 2;
    while(start<=end){
        if(arr[mid] == key){
            return mid;
        }
        else if(arr[mid] > key){
            end = mid-1; 
        }
        else{
            start = mid+1;
        }
        mid = start + (end-start)/2;
    }
    return 0;
}
int main(){
    int arr[5] = {2,3,4,5,6};
    int a = binarySearch(arr,5,8);
    if(a==0)
    cout<<"Element not present"<<endl;
    else
    cout<<"Element found";
    return 0;
}