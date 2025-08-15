#include<iostream>
#include<cstring>
using namespace std;
void reverseString(char str[]){
    int s = 0;
    int e = strlen(str) - 1;
    while(s<e){
        swap(str[s++], str[e--]);
    }
}
bool checkPalindrome(char str[]){
    int s = 0;
    int e = strlen(str) - 1;
    while(s<e){
        if(str[s++] != str[e--]){
            return false;
        }
    }
    return true;
}
int main(){
    char str[100];
    cin>>str;
   reverseString(str);
    cout << str<<endl;
   if(checkPalindrome(str)){
       cout << "Palindrome"<<endl;
   }
   else{
       cout << "Not Palindrome"<<endl;
   }
   return 0;
    return 0;
}