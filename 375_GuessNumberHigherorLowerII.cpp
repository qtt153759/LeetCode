#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int getMoneyAmount(int n) {
                vector<vector<int>> dp(n+1, vector<int>(n+1, 0));


        for(int len=1;len<=n;len++){
            for(int i=1;i+len-1<=n;i++){
                if(len==1){
                    dp[i][i+len-1]=0;//=db[i][i] vì len=1
                    // printf("dp[%d][%d]=%d\n",i,i+len-1,dp[i][i+len-1]);
                }
                else if(len==2){
                    dp[i][i+len-1]=i;//=db[i][i+1] vì len=2
                    // printf("dp[%d][%d]=%d\n",i,i+len-1,dp[i][i+len-1]);
                }
                else{
                    int tmp=INT_MAX;
                    for(int j=i+1;j<i+len-1;j++){
                        //min vì chúng ta sẽ loop j thế nào để 2 bên của j cùng nhỏ=> chỉ có ở giữa thôi binary search
                        tmp=min(tmp,max(j+dp[i][j-1],j+dp[j+1][i+len-1]));
                    }
                    dp[i][i+len-1]=tmp;
                }
                // printf("dp[%d][%d]=%d\n",i,i+len-1,dp[i][i+len-1]);
            }
        }
        return dp[1][n];
    }
};
int main(){
    Solution res;
    cout<<res.getMoneyAmount(10);
}