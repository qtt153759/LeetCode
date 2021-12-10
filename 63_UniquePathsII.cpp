#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int uniquePathsWithObstacles(vector<vector<int>> &obstacleGrid)
    {
        // cout << m << "---" << n << endl;
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        int arr[m + 2][n + 2];
        if (obstacleGrid[0][0] == 1 || obstacleGrid[m - 1][n - 1] == 1)
        {
            return 0;
        }
        for (int i = 0; i <= m + 1; i++)
        {
            arr[i][0] = 0;
            arr[i][n + 1] = 0;
        }
        for (int i = 0; i <= n + 1; i++)
        {
            arr[0][i] = 0;
            arr[m + 1][i] = 0;
        }
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (obstacleGrid[i][j] == 1)
                {
                    arr[i + 1][j + 1] = -1;
                }
                else
                {
                    arr[i + 1][j + 1] = 0;
                }
            }
        }
        arr[1][1] = 1;
        for (int i = 1; i <= m; i++)
        {
            //cout << "row" << i << "  ";
            for (int j = 1; j <= n; j++)
            {
                // cout << arr[i][j] << " ";
                if (arr[i][j] == -1)
                    continue;
                if (arr[i][j + 1] >= 0)
                {
                    arr[i][j + 1] = arr[i][j] + arr[i][j + 1];
                }
                if (arr[i + 1][j] >= 0)
                {
                    arr[i + 1][j] = arr[i][j] + arr[i + 1][j];
                }
            }
            //cout << endl;
        }
        if (arr[m][n] == -1)
        {
            return 0;
        }
        return arr[m][n];
    }
};
int main()
{
    Solution solut;
    vector<vector<int>> obstacleGrid = {{0, 0, 0}, {0, 1, 0}, {0, 0, 0}};
    cout << solut.uniquePathsWithObstacles(obstacleGrid);
}
