#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;
    int row = 1;
    while (row <= n) {
        int space = row - 1;
        while (space) {
            cout << " ";
            space--;
        }
        int col = n;
        while (col >= row) {
            cout <<"*";
            col = col - 1;
        }
        cout << endl;
        row++;
    }
    return 0;
}

