class Solution(object):
    def triangleNumber(self, nums):
        n = len(nums)
        nums = sorted(nums)
        res = 0
        for k in range(2, n):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j - i
                    j -= 1
                else:
                    i += 1
        return res


test = Solution()
print(test.triangleNumber([7, 0, 0, 0]))
