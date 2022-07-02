#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    unsigned long long countGoodNumbers(long long n)
    {
        unsigned long long k = n / 2;
        int t = n % 2;
        unsigned long long res = 1;
        unsigned long long e = 1e9 + 7;
        long long x = 20;
        k = k % (e - 1);

        while (k > 0)
        {
            if (k & 1)
            {
                res = (res * x) % e;
            }
            k = k >> 1;
            x = (x * x) % e;
        }
        //     while (y > 0) {
        //     // If y is odd, multiply x with result
        //     if (y & 1) res = (res*x) % p;

        //     // we have did the odd step is it was odd, now do the even step
        //     y = y>>1; // dividing y by 2, y>>1 is same as y/2
        //     x = (x*x) % p;
        //   }
        res = res * pow(5, t);
        res = res % e;
        return res;
    }
};
int main()
{
    Solution result;
    cout << result.countGoodNumbers(806166225460393);
}