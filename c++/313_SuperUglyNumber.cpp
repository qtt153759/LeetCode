#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        int m=primes.size();
        int dp[n];
        int index[m];
        memset(dp,0,sizeof(dp));
        memset(index,0,sizeof(index));
        dp[0]=1;
        for(int i=1;i<n;i++){
            int tmp=INT_MAX;
            for(int j=0;j<m;j++){
                tmp=min(tmp,primes[j]*dp[index[j]]);
            }
            for(int j=0;j<m;j++){
                if(tmp==primes[j]*dp[index[j]]){
                    index[j]++;
                }
            }
            dp[i]=tmp;
        }
        return dp[n-1];
    }
};
int main(){
    Solution res;
    vector<int>primes={2,7,13,19};
    cout<<res.nthSuperUglyNumber(12,primes);
}