class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            n = -n
            x = 1 / x
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2) * x


if __name__ == "__main__":
    test = Solution()
    print(test.myPow(2.0000, -2))
