#include <string>
#include <iostream>
#include <vector>

using namespace std;
int result=0;
int output=0;
struct trie{
    bool end;
    int again;//해당글자가 몇번 나왔는가
    trie* child[26];
    trie()//초기화
    :end(false),again(1){
        memset(child,0,sizeof(child));
    }
    void insert(char* value){
        if(*value=='\0')end= true;//끝나는 부분일때
        else{
            int current=*value-'a';//문자를 정수로 변환
            if(child[current]==NULL)
                child[current]=new trie();
            else
                child[current]->again++;
            child[current]->insert(value + 1);//다음꺼 삽입

        }
    }
    trie* find(char* value){
        if(*value=='\0'){
            output+=result;
            return this;//문자열의 현재 위치 리턴
        }
        if(result>=1) {//두번째 계층부터
            int tmp=0;
            for(int i=0;i<26;i++){
                if(child[i]!=NULL)
                    tmp++;
            }
            if(tmp==1){
                if(this->again==2)//직전에 다른 하나의 단어가 끝난 경우(ex. go와 gone)
                    result++;
                output+=result;
                return this;
            }
        }
        result++;
        int current=*value-'a';
        if(child[current]==NULL)return NULL;//값 없음
        return child[current]->find(value+1);//그 다음 문자 탐색
    }
};
int main() {
    vector<string> words;
    int answer=0;
    string w;
    trie root;
    while(cin>>w){//ex,[go,gone,guild]
        //ex2.[word,world,war,warrior]
        words.push_back(w);
    }
    for(int i=0;i<words.size();i++){
        root.insert(&words[i][0]);
    }
    for(int i=0;i<words.size();i++){
        result=0;
        root.find(&words[i][0]);
    }
    cout<<output;
    return 0;
}