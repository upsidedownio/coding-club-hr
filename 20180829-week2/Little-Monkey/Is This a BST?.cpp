
struct Node {
    int data;
    Node* left;
    Node* right;
};

bool checkBST(Node* root) {
    Node* now=root;//현재 위치의 노드
    //왼쪽 판별
    while(true){
        if(now->data>now->left->data||now->data<now->right->data){//왼쪽이 now보다 작거나,오른쪽이 now보다 크면
            return false;//false를 리턴
        }
        if(!checkBST(now->right))
            return false;//오른쪽 노드 판별
        if(!checkBST(now->left))
            return false;//왼쪽 노드 판별
        //반복
        if(now== nullptr) {//마지막이면
            break;//탈출
        }
    }
    return true;
}