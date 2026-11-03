#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

void knapsack01(vector<int>& p,vector<int>& wt, int w){
    int max_profit = 0, n = 5;

    vector<vector<int>> dp(n + 1, vector<int>(w + 1,0));

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= w; i++){
            if(wt[i] > w){
                dp[i][j] = dp[i - 1][j];
            }
            else{
                dp[i][j] = max(
                    p[i - 1] + dp[i - 1][j - wt[i - 1]],
                    dp[i - 1][j]
                );
            }
        }
    }
    max_profit = dp[n][w];
    cout << max_profit;

    return;

}


int main(){
    int sack = 40;
    vector<int> profit = {4,6,2,8,3};
    vector<int> weight = {12,15,10,20,9};

    knapsack01(profit, weight, sack);
}