class Solution(object):
    def goodIndices(self, nums, k):
        n = len(nums)
        if k == 1:
            return [i for i in range(1, n - 1)]
        inc = [1 for i in range(n)]
        dec = [1 for i in range(n)]
        res = []
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1
            if nums[n - i] < nums[n - i - 1]:
                dec[n - i - 1] = dec[n - i] + 1
        for i in range(k, n - k):
            if inc[i - 1] < k and dec[i + 1] < k:
                res.append(i)
        return res


test = Solution()
print(test.goodIndices([388589, 17165, 726687, 401298, 600033, 537254, 301052, 151069, 399955], 4))
