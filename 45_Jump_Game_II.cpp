#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int jump(vector<int> &nums)
    {
        int n = nums.size();
        int arr[n] = {0};
        for (int i = 0; i < n - 1; i++)
        {
            // cout << "xet i= " << i << endl;
            for (int j = 1; j <= nums[i] && i + j < n; j++)
            {
                //cout << "xet arr i " << i << " va arr i+j " << i + j << "  " << arr[i] << "---------" << arr[i + j] << endl;
                if (arr[i + j] == 0)
                {
                    arr[i + j] = arr[i] + 1;
                }
                else
                {
                    arr[i + j] = min(arr[i + j], arr[i] + 1);
                }
            }
            //cout << arr[i] << endl;
        }
        return arr[n - 1];
    }
};
int main()
{
    Solution solution;
    vector<int> nums = {3, 2, 1, 0, 4};
    cout << solution.jump(nums);
}