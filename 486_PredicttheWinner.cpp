#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    bool PredictTheWinner(vector<int> &nums)
    {
        vector<vector<pair<int, int>>> arr;
        for (int i = 0; i < nums.size(); i++)
        {
            vector<pair<int, int>> tmp;
            for (int j = 0; j < nums.size(); j++)
            {
                tmp.push_back({0, 0});
            }
            arr.push_back(tmp);
        }
        for (int i = 0; i < nums.size(); i++)
        {
            arr[i][i].first = nums[i];
            arr[i][i].second = 0;
        }
        pair<int, int> result = assume(nums, 0, nums.size() - 1, arr);
        if (result.first >= result.second)
        {
            for (int i = 0; i < nums.size(); i++)
            {
                for (int j = 0; j < nums.size(); j++)
                {
                    cout << arr[i][j].first << "-" << arr[i][j].second << "          ";
                }
                cout << endl;
            }
            return true;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = 0; j < nums.size(); j++)
            {
                cout << arr[i][j].first << "-" << arr[i][j].second << "          ";
            }
            cout << endl;
        }
        return false;
    }
    pair<int, int> assume(vector<int> &nums, int start, int end, vector<vector<pair<int, int>>> &arr)
    {
        if (arr[start][end].first != 0)
        {
            return arr[start][end];
        }
        int chooseBegin = nums[start] + assume(nums, start + 1, end, arr).second;
        int chooseLast = nums[end] + assume(nums, start, end - 1, arr).second;
        if (chooseBegin > chooseLast)
        {
            arr[start][end].first = chooseBegin;
            arr[start][end].second = arr[start + 1][end].first;
        }
        else
        {
            arr[start][end].first = chooseLast;
            arr[start][end].second = arr[start][end - 1].first;
        }
        return arr[start][end];
    }
};
int main()
{
    Solution res;
    vector<int> vect = {4, 8, 12, 16};
    cout << res.PredictTheWinner(vect);
}