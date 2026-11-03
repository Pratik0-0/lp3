#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

struct ele{
    int wt;
    int pf;
    double ratio;
};


bool comapre(ele a, ele b){
    return a.ratio > b.ratio;
}
int main(){

    int sack = 40;
    vector<int> profit = {4,6,2,8,3};
    vector<int> weight = {12,15,10,20,9};
    ele data[5];
    for(int i = 0; i < 5;i++){
        data[i].wt = weight[i];
        data[i].pf = profit[i];
        data[i].ratio =  (double)profit[i] / weight[i];
    }

    sort(data, data + 5, comapre);

    for(int i =0; i < 5; i++){
        cout << data[i].wt << " "<< data[i].pf << " "<< data[i].ratio << " "<<endl;
    }
    double max_profit = 0;
    for(int i =0; i < 5; i++){
        if(sack == 0)   break;
        if(data[i].wt <= sack){
            sack = sack - data[i].wt;
            
            max_profit += data[i].pf; 
            double r = data[i].ratio;
            cout << "element profit = " << data[i].pf << " weight = " << data[i].wt<< " remaining = " << sack << " ratio = " << r <<endl;
            data[i].wt = 0;
        }else{
            max_profit += data[i].ratio * sack;
            double taken = data[i].ratio * sack ;
            double r = data[i].ratio;
            cout << "element profit = " << data[i].pf << " weight = " << data[i].wt<< " Taken  = " << taken<< " remaining = " << sack << " ratio = " << r << endl;
            sack = 0;
            break;
        }
    }

    cout << max_profit << endl;



    return 0;
}