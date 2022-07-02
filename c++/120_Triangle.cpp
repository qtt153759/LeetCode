#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int minimumTotal(vector<vector<int>> &triangle)
    {
        int n = triangle.size();
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            arr[i] = triangle[n - 1].at(i);
            // cout << arr[i] << " ";
        }
        // cout << endl;
        for (int i = 1; i < n; i++)
        {
            for (int j = 0; j < n - i; j++)
            {
                arr[j] = min(arr[j], arr[j + 1]) + triangle[n - i - 1].at(j);
                // cout << arr[j] << " ";
            }
            // cout << endl;
        }
        return arr[0];
    }
};
int main()
{
    Solution solute;
    vector<vector<int>> nums = {{-10}};
    cout << solute.minimumTotal(nums);
}