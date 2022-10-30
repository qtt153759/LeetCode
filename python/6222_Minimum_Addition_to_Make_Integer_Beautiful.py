from math import floor


class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        def calculate(n):
            total = 0
            while n != 0:
                total += n % 10
                n = floor(n / 10)
            return total

        m = n
        i = 1
        while calculate(m) > target:
            a = m + pow(10, i)
            m = floor(a - a % pow(10, i))
            i += 1
        return int(m - n)


test = Solution()
print(test.makeIntegerBeautiful(n=16, target=6))
