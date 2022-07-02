#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int kthGrammar(int n, int k)
    {
        if (n == 1 || k == 1)
        {
            return 0;
        }
        int x = kthGrammar(n - 1, (k + 1) / 2);
        if (x == 1)
        {
            if (k % 2 == 0)
            {
                return 0;
            }
            else
            {
                return 1;
            }
        }
        else if (x == 0)
        {
            if (k % 2 == 0)
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }
    }
};
int main()
{
    Solution res;
    cout << res.kthGrammar(5, 11);
}