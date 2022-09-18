class Solution(object):
    def longestContinuousSubstring(self, s):
        n = len(s)
        dp = [0 for i in range(n)]
        res = 0
        dp[0] = 1
        for i in range(1, n):
            dp[i] = 1
            if ord(s[i]) - ord(s[i - 1]) == 1:
                dp[i] = dp[i - 1] + 1
        print(dp)
        return max(dp)


test = Solution()
print(test.longestContinuousSubstring("abacaba"))
