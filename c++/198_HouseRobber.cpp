#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> arr;
        int n=nums.size();
        arr.resize(n+1);
        arr[0]=0;
        arr[1]=nums[0];
        int res=0;
        for(int i=2;i<=n;i++){
            arr[i]=max(arr[i-1],arr[i-2]+nums[i-1]);
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