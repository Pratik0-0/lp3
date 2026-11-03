#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>

using namespace std;


struct Node{
    char ch;
    int freq;
    Node * left;
    Node * right;

    Node(char c, int f){
        ch = c;
        freq = f;
        left = NULL;
        right = NULL;
    }
};

struct Compare{
    bool operator() (Node*a , Node*b){
        return a -> freq > b -> freq;
    }
};

void print_codes(Node* root, string code){
    if(!root)   return;
    if(root -> left == NULL && root -> right == NULL){
        cout << "Root : " << root -> ch << "\tcode : " << code << endl;
        return;
    }

    print_codes(root -> left, code + "0");
    print_codes(root -> right, code + "1");
}

int main(){
    vector<char> aplha = {'a','b','c','d','e'};
    vector<int> freq = {4,10,2,32,18};

    priority_queue<Node*, vector<Node*>, Compare> heap;

    for(int i = 0; i < 5; i++){
        heap.push(
            new Node(aplha[i], freq[i])
        );
    }

    //build huffman Tree
    while(heap.size() > 1){
        Node * l = heap.top();
        heap.pop();
        Node * r = heap.top();
        heap.pop();

        Node* parent = new Node('$', l-> freq + r-> freq);
        parent-> right = r;
        parent-> left = l;
        heap.push(parent);
    }
    print_codes(heap.top(), "");

}