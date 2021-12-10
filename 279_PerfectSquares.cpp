#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int numSquares(int n) {
        if(n==1||n==0){
            return n;
        }
        int arr[n+1];
        fill(arr,arr+n+1, 100);
        cout<<arr[1]<<endl;
        arr[0]=0;
        for(int i=1;i<=n;i++){
            for(int j=1;j*j<=i;j++){
                arr[i]=min(arr[i],arr[i-j*j]+1);
            }
           // printf("arr[%d]=%d\n",i,arr[i]);
        }
        return arr[n];
    }
};
int main(){
    Solution result;
    cout<<result.numSquares(12);
}
