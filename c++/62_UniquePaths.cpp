#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int uniquePaths(int m, int n)
    {
        // cout << m << "---" << n << endl;
        int arr[m + 1][n + 1];
        for (int i = 0; i <= m; i++)
        {
            for (int j = 0; j <= n; j++)
            {
                arr[i][j] = 0;
                // cout << arr[i][j] << " ";
            }
            cout << endl;
        }
        arr[1][1] = 1;
        for (int i = 1; i <= m; i++)
        {
            //cout << "row" << i << "  ";
            for (int j = 1; j <= n; j++)
            {
                // cout << arr[i][j] << " ";
                arr[i][j + 1] = arr[i][j] + arr[i][j + 1];
                arr[i + 1][j] = arr[i][j] + arr[i + 1][j];
            }
            //cout << endl;
        }
        return arr[m][n];
    }
};
int main()
{
    Solution solut;
    cout << solut.uniquePaths(3, 7);
}
