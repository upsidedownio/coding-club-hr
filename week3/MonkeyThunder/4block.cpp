//
// Created by DongHoon Kim on 10/09/2018.
//
#include <iostream>

int main(){

    int INT_Array_y, INT_Array_x;
    int INT_BuffNum;

    //m,n 입력
    INT_Array_y = 4; // = m
    INT_Array_x = 5; // = n
    //

    char** Char_IN_Array = new char*[INT_Array_y];
    for(int i0=0;i0<INT_Array_y;i0++){
        Char_IN_Array[i0] = new char[INT_Array_x];
    }

    //게임판 정보 입력
    Char_IN_Array[0] = "CCBDE";
    Char_IN_Array[1] = "AAADE";
    Char_IN_Array[2] = "AAABF";
    Char_IN_Array[3] = "CCBBF";
    //"CCBDE","AAADE","AAABF","CCBBF"


    int** INT_Block_Array = new int*[INT_Array_y];
    int** INT_Buff_Block_Array = new int*[INT_Array_y];


    for(int i0=0;i0<INT_Array_y;i0++){
        INT_Block_Array[i0] = new int[INT_Array_x];
        INT_Buff_Block_Array[i0] = new int[INT_Array_x];
    }

    //입력받은 정보를 Block_Array 로 ASCII화 하여 저장
    for(int i0=0;i0<INT_Array_y;i0++){
        for(int i1=0;i1<INT_Array_x;i1++){
            INT_Block_Array[i0][i1] = Char_IN_Array[i0][i1];
        }
    }

    //블럭 현황 출력
    for(int i0=0;i0<INT_Array_y;i0++){
        for(int i1=0;i1<INT_Array_x;i1++){
            std::cout<<(char)INT_Block_Array[i0][i1];
        }
        std::cout<<std::endl;
    }

    std::cout<<"-------------------"<<std::endl;


    while(true) {

        //사라질 블록을 기록할 Buff Array 초기화
        for(int i0=0;i0<INT_Array_y;i0++){
            for(int i1=0;i1<INT_Array_x;i1++){
                INT_Buff_Block_Array[i0][i1] = 1;
            }
        }
        //

        INT_BuffNum = 99;//break loop

        //2*2로 모여있는 같은 알파벳 탐지하여 INT_Buff_Block_Array에 0으로 기록 x = 0~INT_Array_x-2, y = 0~INT_Array_y-2
        for (int i0 = 0; i0 < INT_Array_y - 1; i0++) {
            for (int i1 = 0; i1 < INT_Array_x - 1; i1++) {
                if (INT_Block_Array[i0][i1] != 0) {
                    if (INT_Block_Array[i0][i1] == INT_Block_Array[i0 + 1][i1] &&
                        INT_Block_Array[i0][i1] == INT_Block_Array[i0][i1 + 1] &&
                        INT_Block_Array[i0][i1] == INT_Block_Array[i0 + 1][i1 + 1]) {
                        INT_Buff_Block_Array[i0][i1] = 0;
                        INT_Buff_Block_Array[i0 + 1][i1] = 0;
                        INT_Buff_Block_Array[i0][i1 + 1] = 0;
                        INT_Buff_Block_Array[i0 + 1][i1 + 1] = 0;
                        INT_BuffNum = 0;
                    }
                }
            }
        }

        //사라질 블럭이 없으면 멈춤
        if(INT_BuffNum!=0){
            break;
        }

        //INT_Buff_Block_Array에 0으로 기록된 블럭을 비우고 낙하시킴 x = 0~INT_Array_x-1, y = INT_Array_y-1~1
        for (int i0 = INT_Array_y - 1; i0 > 0; i0--) {
            for (int i1 = 0; i1 < INT_Array_x; i1++) {

                INT_BuffNum = 0; // 낙하 칸수 기록

                for (int i2 = 0; i2 < i0; i2++) {
                    if (INT_Buff_Block_Array[i0 - i2][i1] == 0) {
                        INT_BuffNum++;
                    }
                    else{
                        break;
                    }
                }

                // 낙하
                if (INT_BuffNum != 0) {
                    INT_Block_Array[i0][i1] = INT_Block_Array[i0 - INT_BuffNum][i1];
                    INT_Block_Array[i0 - INT_BuffNum][i1] = 0;
                    INT_Buff_Block_Array[i0 - INT_BuffNum][i1]=0;
                }
            }
        }
        // 블럭 현황 출력
        for(int i0=0;i0<INT_Array_y;i0++){
            for(int i1=0;i1<INT_Array_x;i1++){
                std::cout<<(char)INT_Block_Array[i0][i1];
            }
            std::cout<<std::endl;
        }

        std::cout<<"-------------------"<<std::endl;
    }

    INT_BuffNum=0;

    //사라진 블럭 숫자 기록
    for(int i0=0;i0<INT_Array_y;i0++){
        for(int i1=0;i1<INT_Array_x;i1++){
            if(INT_Block_Array[i0][i1]==0){
                INT_BuffNum++;
            }
        }
    }


    std::cout<<"Result : "<<INT_BuffNum<<std::endl;



    delete [] Char_IN_Array;
    for(int i0=0;i0<INT_Array_y;i0++){
        delete [] INT_Block_Array[i0];
        delete [] INT_Buff_Block_Array[i0];
    }
    delete [] INT_Block_Array;
    delete [] INT_Buff_Block_Array;

    return 0;
}