#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<int> vect;
    vector<int> diffWaysToCompute(string expression)
    {
        vector<int> res;
        for (int i = 0; i < expression.size(); i++)
        {
            if (expression[i] == '*' || expression[i] == '+' || expression[i] == '-')
            {
                vector<int> left = diffWaysToCompute(expression.substr(0, i));
                vector<int> right = diffWaysToCompute(expression.substr(i + 1));
                for (auto n1 : left)
                {
                    for (auto n2 : right)
                    {
                        if (expression[i] == '*')
                        {
                            res.push_back(n1 * n2);
                        }
                        else if (expression[i] == '-')
                        {
                            res.push_back(n1 - n2);
                        }
                        if (expression[i] == '+')
                        {
                            res.push_back(n1 + n2);
                        }
                    }
                }
            }
        }
        if (res.empty())
        {
            res.push_back(atoi(expression.c_str()));
        }
        return res;
    }
};
int main()
{
    Solution solution;
    vector<int> result = solution.diffWaysToCompute("2*3-4*5");
    for (auto res : result)
    {
        cout << res << " ";
    }
}