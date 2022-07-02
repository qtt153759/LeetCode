#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    // evens  = 0, 2, 4, 6, 8  => 5 evens
    // primes = 2, 3, 5, 7     => 4 primes

    int p = 1e9 + 7;

    // calculating x^y efficeiently
    long long power(long long x, long long y)
    {
        long long res = 1;

        x = x % p; // Update x if it is more than or equal to p
        if (x == 0)
            return 0;
        cout << "Khoi tao mau x" << x << " va y" << y << endl;
        while (y > 0)
        {
            cout << "tai k=" << y << "  ta dc x=" << x << endl;
            if (y & 1)
                res = (res * x) % p;

            // we have did the odd step is it was odd, now do the even step
            y = y >> 1; // dividing y by 2, y>>1 is same as y/2
            x = (x * x) % p;
        }
        return res;
    }

    int countGoodNumbers(long long n)
    {
        long long count_of_4s = n / 2;
        long long count_of_5s = n - count_of_4s;
        long long ans = ((power(20, count_of_4s) % p * power(5LL, n % 2) % p) % p);
        return (int)ans;
    }
};
int main()
{
    Solution solute;
    solute.countGoodNumbers(806166225460393);
}