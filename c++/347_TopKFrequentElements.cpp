#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> m;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (int i = 0; i < nums.size(); i++)
        {
            m[nums[i]]++;
        }
        for (auto it = m.begin(); it != m.end(); it++)
        {
            pq.push({it->second, it->first});
            // cout << "push " << it->second << "   " << it->first << endl;
            if (pq.size() > k)
            {
                // cout << "pop vect " << pq.top().first << "   " << pq.top().second << endl;
                pq.pop();
            }
        }
        vector<int> vect;
        while (!pq.empty())
        {
            vect.push_back(pq.top().second);
            // cout << "push vect " << pq.top().second << endl;
            pq.pop();
        }
        reverse(vect.begin(), vect.end());
        return vect;
    }
};
int main()
{
    Solution solute;
    vector<int> nums = {1, 1, 1, 2, 2, 3};
    int k = 2;
    vector<int> res = solute.topKFrequent(nums, k);
    for (int i = 0; i < res.size(); i++)
    {
        cout << res[i] << " ";
    }
}