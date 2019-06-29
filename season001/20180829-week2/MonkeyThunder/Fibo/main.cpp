#include <iostream>

bool Fibo_Test(int INT_INPUT);

int main() {

    int INT_NumberofData;
    int *INT_Buff;
    INT_Buff=new int[INT_NumberofData];

    std::cin>>INT_NumberofData;

    for(int i0=0;i0<INT_NumberofData;i0++){
        std::cin>>INT_Buff[i0];
    }

    for(int i0=0;i0<INT_NumberofData;i0++){
        if(Fibo_Test(INT_Buff[i0])){
            std::cout<<"IsFibo"<<std::endl;
        }
        else{
            std::cout<<"IsNotFibo"<<std::endl;
        }
    }

}

bool Fibo_Test(int INT_INPUT){

    int INT_FiboNum, INT_Prev_FiboNum;
    int INT_Buff_Num;

    INT_Prev_FiboNum=0;
    INT_FiboNum=1;
    while(true){
        INT_Buff_Num=INT_FiboNum;

        INT_FiboNum=INT_FiboNum+INT_Prev_FiboNum;

        INT_Prev_FiboNum=INT_Buff_Num;

        if(INT_FiboNum>=INT_INPUT){
            break;
        }
    }
    if(INT_FiboNum==INT_INPUT||INT_INPUT==0){
        return true;
    }
    else{
        return false;
    }
}

