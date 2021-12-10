#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int findTheWinner(int n, int k)
    {
        queue<int> Q;
        int x, tmp;
        for (int i = 1; i <= n; i++)
        {
            Q.push(i);
        }
        while (Q.size() != 1)
        {
            x = k - 1;
            while (x > 0)
            {
                tmp = Q.front();
                Q.pop();
                Q.push(tmp);
                x--;
            }
            Q.pop();
        }
        return Q.front();
    }
};
int main()
{
    Solution solute;
    cout << solute.findTheWinner(5, 2);
}