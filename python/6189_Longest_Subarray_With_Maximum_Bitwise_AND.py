class Solution(object):
    def longestSubarray(self, nums):
        currentMax = float("-inf")
        cur = 0
        res = 1
        for num in nums:
            if num > currentMax:
                currentMax = num
                cur = 1
                res = 1
            elif num < currentMax:
                cur = 0
            else:
                cur += 1
                res = max(res, cur)
        return res


test = Solution()
print(test.longestSubarray([96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 279979]))
