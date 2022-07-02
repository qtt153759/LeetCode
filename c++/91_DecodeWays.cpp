#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int numDecodings(string s)
    {
        if (s == "0")
        {
            return 0;
        }
        int n = s.length();
        int arr[n + 1] = {0};
        arr[0] = 1, arr[1] = 1;
        for (int i = 2; i <= n; i++)
        {
            //if ((s[i - 2] <= '2' && s[i - 2] > '0') && (s[i - 1] <= '9' && s[i - 1] > '0'))
            string x = s.substr(i - 1, 1);
            string y = s.substr(i - 2, 2);
            //cout << x << " va  " << y << endl;
            if (x <= "9" && x >= "1")
            {
                arr[i] += arr[i - 1];
                // cout << arr[i] << "------1-----" << arr[i - 1] << endl;
            }
            if (y <= "26" && y >= "10")
            {
                arr[i] += arr[i - 2];
                // cout << arr[i] << "------2-----" << arr[i - 2] << endl;
            }
        }
        return arr[n];
    }
};
int main()
{
    Solution res;
    cout << res.numDecodings("123");
}