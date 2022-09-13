class Solution(object):
    def wiggleMaxLength(self, nums):
        left = 1
        res = 1
        while left < len(nums):
            if nums[left] == nums[left - 1]:
                left += 1
                continue
            break
        if left == len(nums):
            return 1
        current = not (True if nums[left] - nums[left - 1] > 0 else False)
        for i in range(left, len(nums)):
            print("check", i, nums[i], current, nums[i] - nums[i - 1] > 0)
            if (nums[i] - nums[i - 1] > 0) != current and (nums[i] != nums[i - 1]):
                res += 1
                current = not current
        return res


test = Solution()
print(test.wiggleMaxLength([1, 1, 1, 2, 2, 2, 1, 1, 1, 3, 3, 3, 2, 2, 2]))
