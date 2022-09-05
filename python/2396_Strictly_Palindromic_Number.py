import math


class Solution(object):
    def isStrictlyPalindromic(self, n):

        for i in range(2, n - 1):
            remain = n
            res = []
            while remain > 0:
                res.append(remain % i)
                remain //= i
            print(res, i)
            for i in range(len(res) // 2):
                if res[i] != res[len(res) - 1 - i]:
                    return False
        return True


if __name__ == "__main__":
    test = Solution()
    print(test.isStrictlyPalindromic(4))
