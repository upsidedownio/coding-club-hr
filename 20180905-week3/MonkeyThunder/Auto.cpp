//
// Created by DongHoon Kim on 10/09/2018.
//

#include <iostream>
#include <string>


int main(){

    int INT_Word_Num, INT_Counting_Word;
    int INT_BuffNum, INT_Return, INT_BuffExtraAdd;

    int INT_NumofAlphabet[26];

    INT_Word_Num = 4;

    std::string STR_IN_Word[INT_Word_Num];

    //Data In
    STR_IN_Word[0]="gon";
    STR_IN_Word[1]="gone";
    STR_IN_Word[2]="guild";
    STR_IN_Word[3]="g";
    //

    INT_Counting_Word=0;
    INT_Return=0;

    while(true){
        //Initialization
        for(int i0=0;i0<26;i0++){
            INT_NumofAlphabet[i0]=0;
        }
        //

        //각 단어별 (INT_Counting_Word)번째 알파벳 분포 조사
        for(int i0=0;i0<INT_Word_Num;i0++){
            if(STR_IN_Word[i0].size()>INT_Counting_Word){
                INT_BuffNum=STR_IN_Word[i0][INT_Counting_Word];
                INT_NumofAlphabet[INT_BuffNum-97]++;//a=97~z=122 on ASCII
            }

        }
        //

        //같은 알파벳이 있는 경우 기록
        INT_BuffNum=0;
        for(int i0=0;i0<26;i0++){
            if(INT_NumofAlphabet[i0]!=1){
                INT_BuffNum=INT_BuffNum+INT_NumofAlphabet[i0];
            }
        }
        //

        //같은 알파벳이 없는 경우, 마지막 구분을 위해 알파벳의 종류를 더하고 끝냄.
        if(INT_BuffNum==0){
            INT_BuffExtraAdd=0;
            for(int i0=0;i0<26;i0++){
                if(INT_NumofAlphabet[i0]==1){
                    INT_BuffExtraAdd++;
                }
            }
            INT_Return=INT_Return+INT_BuffExtraAdd;

            break;
        }

        INT_Return=INT_Return+INT_BuffNum+INT_BuffExtraAdd;

        INT_Counting_Word++;
    }

    std::cout<<INT_Return<<std::endl;

    return 0;
}