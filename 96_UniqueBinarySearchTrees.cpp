#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int numTrees(int n)
    {
        int arr[n + 1];
        arr[0] = 1, arr[1] = 1;
        arr[2] = 2;
        for (int i = 3; i <= n; i++)
        {
            arr[i] = 0;
            for (int j = 0; j < i; j++)
            {
                arr[i] += arr[j] * arr[i - j - 1];
            }
            cout << arr[i] << " ";
        }
        //cout << endl;
        return arr[n];
    }
};
int main()
{
    Solution solute;
    cout << solute.numTrees(6);
}