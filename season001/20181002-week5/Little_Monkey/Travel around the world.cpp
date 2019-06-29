#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int N,C;//N=도시갯수,C=연료 최대용량

vector<int>a;//기름+
vector<int>b;//기름-
int cnt=0;//시작할수 있는 도시 갯수
int chk(int c){
    vector<pair<int,int>>city;
    for(int i=c;i<N;i++)//c번 도시부터 N-1번 도시까지 우선 저장
        city.push_back(make_pair(a[i],b[i]));
    if(c!=0){//맨처음부터 맨끝까지 저장한게 아닌경우(ex. 2 3 1을 저장해야 할 경우)
        for(int i=0;i<c;i++){
            city.push_back(make_pair(a[i],b[i]));
        }
    }
    //판별 단계
    int oil=0;
    int i=0;
    while(i<N){
        oil+=city[i].first;//해당 도시에서 얻는 기름
        oil-=city[i].second;//다음 도시로 가려면 써야하는 기름
        if(oil<0)
            return 0;
        i++;
    }
    return 1;
}

int main(){
    cin>>N>>C;

    for(int i=0;i<N;i++){//a입력
        int tmp;
        cin>>tmp;
        a.push_back(tmp);
    }
    for(int i=0;i<N;i++){//b입력
        int tmp;
        cin>>tmp;
        b.push_back(tmp);
    }

    for(int i=0;i<N;i++){
        cnt+=chk(i);//i번 도시에서 시작할 때
    }

    cout<<cnt;

    return 0;
}