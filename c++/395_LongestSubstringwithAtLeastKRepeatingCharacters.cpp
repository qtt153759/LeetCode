#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int longestSubstring(string s, int k)
    {
        if (s.size() < k)
        {
            return 0;
        }
        unordered_map<char, int> m;
        for (int i = 0; i < s.size(); i++)
        {
            m[s[i]]++;
        }
        int res1, res2;
        for (int i = 0; i < s.size(); i++)
        {
            if (i == s.size() - 1)
            {
                return s.size();
            }
            if (m[s[i]] < k)
            {
                res1 = longestSubstring(s.substr(0, i), k);
                res2 = longestSubstring(s.substr(i + 1), k);
                return max(res1, res2);
            }
        }
    }
};
int main()
{
    Solution res;
    cout << res.longestSubstring("weiton", 2);
}
