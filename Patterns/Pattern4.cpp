#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of rows: ";
    cin >> n;
    int row = 1;
    while (row <= n) {
        char start = 'A' + n - row;
        int col = 1;
        while (start <= 'A' + n - 1) {
            cout << start << " ";
            start = start + 1;
            col = col + 1;
        }
        cout << endl;
        row = row + 1;
    }
    return 0;
}