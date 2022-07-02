#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n=prices.size();
        vector<int>rest(prices.size(), 0);
        vector<int>buy(prices.size(), 0);
        vector<int>sell(prices.size(), 0);
        rest[0]=0;
        buy[0]=-prices[0];
        sell[0]=0;
        for(int i=1;i<n;i++){
            rest[i]=max(rest[i-1],sell[i-1]);//(rest,sell)=>rest
            buy[i]=max(rest[i-1]-prices[i],buy[i-1]);//(rest-prices,buy)=>uy
            sell[i]=buy[i-1]+prices[i];//(buy+prices)=>sell
        }
        return max(rest[n-1],sell[n-1]);
        
    }
};
int main(){
    Solution res;
    vector<int>prices={1,2,3,0,2};
    cout<<res.maxProfit(prices);
}