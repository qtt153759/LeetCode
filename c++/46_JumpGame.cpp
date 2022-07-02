#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        int n = nums.size();
        bool arr[n];
        for (int i = 1; i < n; i++)
        {
            arr[i] = false;
        }
        arr[0] = true;
        for (int i = 0; i < n - 1; i++)
        {
            if (arr[i] == true)
            {
                for (int j = nums[i]; j > 0; j--)
                {
                    if (arr[i + j] == true)
                    {
                        break;
                    }
                    else
                    {
                        arr[i + j] = true;
                    }
                }
            }
        }
        return arr[n - 1];
    }
};
int main()
{
    Solution solution;
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << solution.canJump(nums);
}