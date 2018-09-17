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

    String_Test="33579";

    result = twoTwo(String_Test);

    cout<<"Result = "<<result<<endl;

    return 0;
}



int twoTwo(string a){

    int INT_Result, INT_BetNum;

    INT_Result=0;

    for(int i0=0;i0<a.size();i0++){
        for(int i1=i0;i1<a.size();i1++){
            INT_BetNum = 0;
            for(int i2=0;i2<(i1-i0+1);i2++){
                INT_BetNum = INT_BetNum * 10 + (a[i2+i0]-48) ;
                if(INT_BetNum==0){
                    break;
                }
            }

            cout<<"i0 = "<<i0<<", i1 = "<<i1<<" Num = "<<INT_BetNum<<endl;

            while(true){
                if(INT_BetNum%2!=0||INT_BetNum==0){
                    break;
                }
                INT_BetNum=INT_BetNum/2;
                if(INT_BetNum==1){
                    INT_Result++;
                    cout<<"i0 = "<<i0<<", i1 = "<<i1<<" Result Num = "<<INT_Result<<endl;

                    break;
                }
            }

        }
    }

    //a.size();

    return INT_Result;
}