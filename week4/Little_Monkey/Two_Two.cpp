#include <iostream>
#include <vector>
#include <string>
using namespace std;

int pow_2[18];
vector<string> s;

int strength(int i,int p,int k){
    if(s[i][p]-'0'==0)
        return 0;
    int value=0;
    for(int n=p;n<=k;n++){
        value=value*10+(s[i][n]-'0');
    }
    return value;
}

int main(){
    int N;
    int tmp=1;
    cin>>N;//입력할 배열 갯수
    s.resize(N);
    for(int i=0;i<N;i++){//배열 입력
        cin>>s[i];
    }
    for(int p=0;p<18;p++){
        tmp*=2;
        pow_2[p]=tmp;
    }
    for(int i=0;i<N;i++){//0번 배열부터 N-1번 배열까지
        int cnt=0;//i번 배열에 대한 결과값
        for(int p=0;p<s[i].size();p++){//해당 배열의 p번째글자부터 마지막 글자까지
            for(int k=p;k<s[i].size();k++){//p~k번째 글자까지
                int t= strength(i,p,k);//숫자를 만든다
                for(int q=0;q<18;q++){
                    if(t==pow_2[q])
                        cnt++;
                }
            }
        }
        cout<<cnt<<endl;
    }

    return 0;
}