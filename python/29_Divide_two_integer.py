class Solution(object):
    def divide(self, dividend, divisor):
        isSameSign = (dividend > 0) == (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        while dividend >= divisor:
            i, tmp = 1, divisor
            while dividend >= tmp:
                i <<= 1
                tmp <<= 1
            tmp >>= 1
            i >>= 1
            ans += i
            dividend -= tmp
            print(dividend, tmp)

        print(isSameSign)
        if not isSameSign:
            ans = -ans
        return min(max(-2147483648, ans), 2147483647)  # trong khoang (2^-32,2^32) nen ko tinh -2147483648


if __name__ == "__main__":
    test = Solution()
    print(test.divide(10, 3))
