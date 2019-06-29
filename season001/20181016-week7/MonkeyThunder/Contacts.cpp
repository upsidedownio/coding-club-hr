#include <iostream>
#include <string.h>
using namespace std;


int main() {

    int INT_NumberOfName = 0;
    int INT_Return = 0;
    int INT_NumberOfCommand;
    cin >> INT_NumberOfCommand;

    string *CHR_Command = new string[2 * INT_NumberOfCommand];
    string *CHR_Name = new string[INT_NumberOfCommand];


    for (int i0 = 0; i0 < 2 * INT_NumberOfCommand; i0++) {
        cin >> CHR_Command[i0];
    }

    for (int i0 = 0; i0 < INT_NumberOfCommand; i0++) {
        if (CHR_Command[2 * i0].compare("add") == 0) {
            CHR_Name[INT_NumberOfName] = CHR_Command[2 * i0 + 1];
            INT_NumberOfName++;
        }
        if (CHR_Command[2 * i0].compare("find") == 0) {
            for (int i1 = 0; i1 < INT_NumberOfName; i1++) {
                if (strstr(CHR_Name[i1].c_str(), CHR_Command[2 * i0 + 1].c_str())) {
                    INT_Return++;
                }
            }
            cout << INT_Return << endl;
            INT_Return = 0;
        }
    }


    delete[] CHR_Command;
    delete[] CHR_Name;

    return 0;
}