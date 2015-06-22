/*

Write a method to point the last K liens of an input file using C++.

- open the file.
- use k string objects to cache k lines, update the oldest ones with
  newly `getline` content.
- print the strings.

NOTE: there is a `\n` at end of file, so there might seems one line
fewer than expected.

*/

#include <iostream>
#include <fstream>
using namespace std;

#define k 3

int main() {
    ifstream file;
    string lines[k];
    file.open("sample.txt");
    int i = 0; // indicator of oldest line
    if (file.is_open()) {
        // read file into lines, circularly.
        while (getline(file, lines[i])) {
            cout << lines[i] << endl;;
            i++;
            i = i % k;
        }

        // print last k lines
        for (int j = 0; j < k; j++) {
            cout << lines[(i + j) % k] << endl;
        }

        file.close();
    }

    return 0;
}
