#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int integerBreak(int n) {
        vector<int>arr(n+1,0);
        arr[1]=1;
        for(int i=2;i<=n;i++){
            for(int j=1;j<i;j++){
                arr[i]=max(arr[i],max(arr[j],j)*max(i-j,arr[i-j]));
            }                 
        }
        return arr[n];
    }
};
int main(){
    Solution res;
    cout<<res.integerBreak(10);
}