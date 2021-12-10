#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int m = matrix[0].size();
        int n = matrix.size();
        int i = 0;
        int j = m - 1;
        while (0 <= j && i < n)
        {
            if (matrix[i][j] > target)
            {
                j--;
            }
            else if (matrix[i][j] < target)
            {
                i++;
            }
            else if (matrix[i][j] == target)
            {
                return true;
            }
        }
        return false;
    }
};
