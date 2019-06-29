
struct Node{
    int data;
    Node* left;
    Node* right;
};

bool checkBST(Node* root){

    int Min, Max;

    Node* Buff_struct;

    Buff_struct=root;

    Min=0;
    Max=10000;

    while(true){
        if(Buff_struct->data>Min||Buff_struct->data>Max){
            return false;
        }
        Min=root->data;
        Buff_struct=root->left;

        if(Buff_struct==nullptr){
            break;
        }
    }

    while(true){
        if(Buff_struct->data>Min||Buff_struct->data>Max){
            return false;
        }
        Max=root->data;
        Buff_struct=root->right;

        if(Buff_struct== nullptr){
            break;
        }
    }



}