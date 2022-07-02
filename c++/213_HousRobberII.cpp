#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        return max(Solve(nums,0,nums.size()-1),Solve(nums,1,nums.size()));
    }
    int Solve(vector<int>& nums,int l,int r){
        // printf("%d %d\n",l,r);
        vector<int> arr;
        int n=nums.size();
        if(n==1){
            return nums[0];
        }else if(n==0){
            return 0; 
        }
        arr.resize(n+1);
        arr[l]=0;
        arr[l+1]=nums[l];
        int res=arr[l+1];
        for(int i=l+2;i<=r;i++){
            arr[i]=max(arr[i-1],arr[i-2]+nums[i-1]);
            // printf("arr[%d]=%d\n",i,arr[i]);
            res=max(arr[i],res);
        }
        return res;
    }
};

int main(){
    Solution res;
    vector<int> nums={1,2,3,1};
    cout<<res.rob(nums);
}