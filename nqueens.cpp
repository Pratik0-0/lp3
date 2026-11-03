#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

bool possible(int row, int col, vector<int> &board){
    for(int i = 0; i < row; i++){
        if(board[i] == col)  return false;//same col
        if(abs(board[i] - col) == abs(i - row)) return false;//diagonal
    }

    return true;
}

void nqueens(int n, int row, vector<int> &board){
    if(row == n){
        //print

        for(int i =0 ; i < n; i++){
            for(int j =0 ; j < n; j++){
                if(board[i] == j){
                    cout << "\tQ\t";
                }else{
                    cout << "\t.\t";
                }
            }
            cout << endl;
        }

        cout << "---------------------------------------" << endl;
    }
    for(int col = 0; col < n; col++){
        if(possible(row, col, board)){
            board[row] = col;

            nqueens(n, row + 1, board);

            board[row] = -1;
        }

    }
}

int main(){
    int n;
    cin >> n;
    vector<int> board(n,-1);
    nqueens(n,0, board);
    return 0;
}

