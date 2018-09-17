//
// Created by DongHoon Kim on 17/09/2018.
//

#include <iostream>
#include <string>

using namespace std;

int twoTwo(string a);

int main(){

    string String_Test;

    int result;

    String_Test="22222222222222222222";

    result = twoTwo(String_Test);

    cout<<"Result = "<<result<<endl;

    return 0;
}



int twoTwo(string a){

    int INT_Result, INT_BetNum;
    int INT_BuffNum,INT_BuffSum;
    string Str_Buff;

    //Str_Buff=a;

    INT_Result=0;

    for(int i0=0;i0<a.size();i0++) {
        for (int i1 = i0; i1 < a.size(); i1++) {

            for (int i2 = i0; i2 < i1 + 1; i2++) {
                Str_Buff[i2] = a[i2];
            }

            if(Str_Buff[i0]==48){
                break;
            }


            while (true) {

                for (int i2 = i0; i2 < i1 + 1; i2++) {
                    INT_BetNum = Str_Buff[i2] - 48;
                    Str_Buff[i2] = ((INT_BetNum + INT_BuffNum) / 2) + 48;
                    INT_BuffNum = 0;
                    if (INT_BetNum % 2 == 1) {
                        INT_BuffNum = 10;
                    }
                }

                INT_BuffSum = 0;
                for (int i2 = i0; i2 < i1 + 1; i2++) {
                    INT_BuffSum = INT_BuffSum + ((int) Str_Buff[i2] - 48);
                }
                //cout << "INT_BuffSum = " << INT_BuffSum << ", i0 = " << i0 << ", i1 = " << i1 << endl;
                //cout<<"INT_BetNum = "<<INT_BetNum<<", "<<Str_Buff[i0+i2]<<", BuffNum = "<<INT_BuffNum<<endl;
                if (INT_BuffSum == 1) {
                    INT_Result++;
                    break;
                }
                if (Str_Buff[i1] % 2 == 1) {
                    break;
                }
            }
        }
    }

    return INT_Result;
}