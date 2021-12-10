#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<string> list;
    string option = "()";
    int open, close, n;
    vector<string> generateParenthesis(int t)
    {
        n = t;
        open = 0;
        close = 0;
        cout << endl;
        Solve(1, "");
        return list;
    }
    bool check(char Parenthesis)
    {
        if (Parenthesis == '(' && open < n)
        {
            open++;
            return true;
        }
        else if (Parenthesis == ')' && close < open)
        {
            close++;
            return true;
        }
        return false;
    }
    void Solve(int k, string tmp)
    {
        for (int i = 0; i <= 1; i++)
        {
            // cout << "check " << option[i] << " ";
            if (check(option[i]))
            {
                if (k == 2 * n)
                {
                    tmp = tmp + option[i];
                    cout << tmp << endl;
                    list.push_back(tmp);
                }
                else
                {
                    tmp = tmp + option[i];
                    Solve(k + 1, tmp);
                }
                if (option[i] == '(')
                {
                    open--;
                }
                else
                {
                    close--;
                }
                tmp.pop_back();
            }
        }
    }
};
int main()
{
    Solution solution;
    vector<string> vect = solution.generateParenthesis(3);
    for (auto s : vect)
    {
        cout << s << endl;
    }
}