from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        s = -1
        sum = 0
        for i in range(len(nums)):
            if nums[i] < k:
                s = i
                break
        if s == -1:
            return 0
        res = 0
        windowSize = 0
        sum = 1

        for i in range(s, len(nums)):
            while sum * nums[i] >= k and s < i:
                sum = sum // nums[s]
                s = s + 1
                windowSize -= 1
            if sum * nums[i] < k:
                windowSize += 1
                sum = sum * nums[i]
                res = res + windowSize
            else:
                s = s + 1
                sum = 1

        return res


test = Solution()
print(test.numSubarrayProductLessThanK([57, 44, 92, 28, 66, 60, 37, 33, 52, 38, 29, 76, 8, 75, 22], 18))
