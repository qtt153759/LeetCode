class Solution(object):
    def mostFrequentEven(self, nums):
        d = {}
        l = 0
        res = -1
        while l < len(nums):
            if nums[l] % 2 == 0:
                d[nums[l]] = 1
                res = [nums[l], 1]
                break
            l = l + 1
        if res == -1:
            return -1
        for i in range(l + 1, len(nums)):
            if nums[i] % 2 == 1:
                continue
            if nums[i] not in d:
                d[nums[i]] = 0
            d[nums[i]] += 1
            if d[nums[i]] > res[1] or (d[nums[i]] == res[1] and nums[i] < res[0]):
                res = [nums[i], d[nums[i]]]
        return res[0]


test = Solution()
print(test.mostFrequentEven([0, 0, 0, 0]))
