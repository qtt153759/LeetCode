#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int nthUglyNumber(int n) {
        if(n<=0) return 0;
        else if(n==1) return 1;
        int t2=0,t3=0,t5=0;
        int k[n];
        k[0]=1;
        //nguyen ly la moi so tu nhien deu co the chia het cho so nguyen to
        for(int i=1;i<n;i++){
            k[i]=min({k[t2]*2,k[t3]*3,k[t5]*5});
            if(k[i]%2==0) t2++;
            if(k[i]%3==0) t3++;
            if(k[i]%5==0) t5++;
            // printf("k[%d]=%d\n",i,k[i]);
        }
        return k[n-1];
    }
};
int main(){
    Solution res;
    cout<<res.nthUglyNumber(10);
}