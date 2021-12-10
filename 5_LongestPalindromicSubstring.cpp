#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    string longestPalindrome(string s)
    {
        int n = s.length();
        int maxLength = 1;
        int start = 0, end = 1;
        int db[s.length()][s.length()];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                db[i][j] = 0;
            }
        }
        for (int i = 0; i < s.length(); i++)
        {
            db[i][i] = 1; //tu co 1 chu luon luon dung
            if (s[i] == s[i + 1])
            { //xet tu co 2 chu
                db[i][i + 1] = 1;
                if (2 > maxLength)
                {
                    maxLength = 2;
                    start = i;
                    end = i + 1;
                }
            }
        }
        int i, j, counter;
        for (counter = 2; counter < n; counter++)
        {
            for (j = counter, i = 0; j < n; j++, i++) //phai ngan cach giua 2 bien =',' khong thi loi
            {
                if (s[i] == s[j] && db[i + 1][j - 1] == 1)
                {
                    db[i][j] = 1;
                    if (j - i + 1 > maxLength)
                    {
                        maxLength = j - i + 1;
                        start = i;
                        end = j;
                    }
                    //printf("Start:%d  end:%d\n", start, end);
                }
            }
        }

        return s.substr(start, maxLength);
    }
};
class Solution1
{
public:
    string longestPalindrome(string s)
    {
        int n = s.length();

        // corner case
        if (n == 0 || n == 1)
            return s;

        vector<vector<int>> dp(n, vector<int>(n, 0));
        int max_len = 0;
        int max_sid = 0;
        int max_eid = 0;

        int i, j, counter;
        // because every sigle element is palindrome in it self
        for (i = 0; i < n; i++)
            dp[i][i] = 1;

        // for checking the palindrome of length two
        for (j = 1, i = j - 1; j < n; j++, i++)
        {
            if (s[i] == s[j])
            {
                dp[i][j] = 1;
                if (abs(j - i) > max_len)
                {
                    max_len = abs(j - i);
                    max_sid = i;
                    max_eid = j;
                }
            }
        }

        // dynamic programming bottom up approch
        for (counter = 2; counter < n; counter++)
        {
            for (j = counter, i = 0; j < n; j++, i++)
            {
                // cout<<"i="<<i<<", j="<<j<<endl;
                if (s[i] == s[j] && dp[i + 1][j - 1] == 1)
                {
                    dp[i][j] = 1;
                    if (abs(j - i) > max_len)
                    {
                        max_len = abs(j - i);
                        max_sid = i;
                        max_eid = j;
                    }
                }
            }
        }

        // for(int i=0;i<n;i++){
        //     for(int j=0;j<n;j++){
        //         cout<<dp[i][j]<<" ";
        //     }cout<<endl;
        // }
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cout << dp[i][j] << " ";
            }
            cout << endl;
        }
        // cout<<max_sid<<" -- "<<max_eid<<endl;
        return s.substr(max_sid, max_eid - max_sid + 1);
    }
};

int main()
{
    Solution res;
    cout << res.longestPalindrome("aacabdkacaa");
}