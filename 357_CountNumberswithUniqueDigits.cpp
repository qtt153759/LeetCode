#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if(n==0) return 1;
        vector<int>dp;
        dp.resize(n+1);
        dp[1]=10;
        for(int i=2;i<=n;i++){
            dp[i]=9;
            for(int j=1;j<i;j++){
                dp[i]=dp[i]*(10-i);
                //câu này chỉ có phân tích số học thôi dp[i]=dp[i-1]+9*forLoop((10-i))
                //f(1) =>{0,1,2,..,9} =>10 số
                //f(2) = f(1)+(Xét có số 0 hàng đv =>9*1) +(ko có số 0 =>9*8)  => tổng là 9*9
                //f(3) =f(2) +(xét có số 0 hàng đv =>9*9*1) +(xét có số 0 hàng chục => 9*8) +(ko có số 0 nào =>9*8*7)=> tổng là 9*9*8
            }
            dp[i]=dp[i]+dp[i-1];
        }
        return dp[n];
        
    }
};
int main(){
    Solution res;

    // cout<<res.maxProfit(prices);
}