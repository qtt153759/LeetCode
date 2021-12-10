#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int maxProfit = 0;

        for (int i = 1; i < prices.size(); ++i)
            maxProfit += max(prices[i] - prices[i - 1], 0);

        return maxProfit;
    }
};
int main()
{
    Solution res;
    vector<int> prices = {1, 2, 3, 4, 5, 4, 3, 6, 7};
    cout << res.maxProfit(prices);
}