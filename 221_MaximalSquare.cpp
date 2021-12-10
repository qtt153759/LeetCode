#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m=matrix.size();
        int n=matrix[0].size();
        int arr[m+1][n+1];
        memset(arr, 0, sizeof arr); 
        int res=arr[0][0];
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(matrix[i][j]=='0'){
                    arr[i+1][j+1]=0;
                }else if(matrix[i][j]=='1'){
                    arr[i+1][j+1] = min({arr[i][j+1], arr[i+1][j], arr[i][j]}) + 1;
                }
                res=max(res,arr[i+1][j+1]);
                printf("%d ",arr[i+1][j+1]);
            }
            cout<<endl;
        }
        return res*res;
    }
};
int main(){
    Solution res;
    vector<vector<char>> matrix=
    {{'1','1','1','1','0'},{'1','1','1','1','0'},{'1','1','1','1','1'},{'1','1','1','1','1'},{'0','0','1','1','1'}};
    cout<<res.maximalSquare(matrix);

}