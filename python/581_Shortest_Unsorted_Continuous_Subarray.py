class Solution(object):
    def findUnsortedSubarray(self, nums):
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)


test = Solution()
print(test.findUnsortedSubarray([1, 2, 3, 4]))
