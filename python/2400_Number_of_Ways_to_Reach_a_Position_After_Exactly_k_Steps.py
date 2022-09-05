import math


class Solution(object):
    dp = [[-1 for i in range(3010)] for j in range(1010)]

    def numberOfWays(self, startPos, endPos, k):
        if endPos - startPos > k:
            return 0
        if (k - endPos + startPos) % 2 != 0:
            return 0
        return self.way(startPos, endPos, k)

    def way(self, s, e, k):
        if s == e and k == 0:
            return 1
        if k == 0:
            return 0
        if self.dp[s + 1000][k] != -1:
            return self.dp[s + 1000][k]

        self.dp[s + 1000][k] = math.floor((self.way(s - 1, e, k - 1) + self.way(s + 1, e, k - 1)) % 10e7)
        print(self.dp[s + 1000][k])

        return self.dp[s + 1000][k]


if __name__ == "__main__":
    test = Solution()
    print(test.numberOfWays(startPos=1, endPos=2, k=3))
