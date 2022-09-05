class Solution:
    def longestNiceSubarray(self, nums):
        AND = nums[0]
        l = 0
        res = 1
        for r in range(1, len(nums)):
            while AND & nums[r]:
                AND ^= nums[l]
                l += 1
            AND |= nums[r]
            res = max(res, r - l + 1)
        return res


test = Solution()
test.longestNiceSubarray([1, 3, 8, 48, 10])
