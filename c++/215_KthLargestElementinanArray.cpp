#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int i = 0; i < nums.size(); i++)
        {
            pq.push(nums[i]);
            if (pq.size() > k)
            {
                pq.pop();
            }
        }
        return pq.top();
    }
};
int main()
{
    Solution solution;
    vector<int> v = {3, 2, 3, 1, 2, 4, 5, 5, 6};
    cout << solution.findKthLargest(v, 4);
}