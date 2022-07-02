#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    char findKthBit(int n, int k)
    {
        findAnotherKthBit(n, k - 1);
    }
    char findAnotherKthBit(int n, int k)
    {
        // cout << "xet n " << n << " va k" << k << endl;
        int length = pow(2, n) - 1;
        int mid = length / 2;
        if (k == mid)
        {
            if (n == 1)
            {
                return '0';
            }
            // cout << "charactor tai n " << n << " va k" << k << endl;
            // cout << "mid" << endl;
            return '1';
        }
        else if (k < mid)
        {
            return findAnotherKthBit(n - 1, k);
        }
        else if (k > mid)
        {
            char charac = findAnotherKthBit(n - 1, length - 1 - k);
            if (charac == '1')
            {
                // cout << "charactor tai n " << n << " va k" << k << endl;
                // cout << "1->0";
                return '0';
            }
            else
            {
                // cout << "charactor tai n " << n << " va k" << k << endl;
                // cout << "0->1";
                return '1';
            }
        }
    }
};
int main()
{
    Solution solution;
    cout << solution.findKthBit(3, 7);
}