class Solution:
    def minSubArrayLen(self, target, nums):
        if nums == None or len(nums) == 0:
            return 0
        if nums[0] >= target:
            return 1

        start = 0
        end = 0
        window_sum = 0
        minimum = 10**10000

        while end < len(nums):
            if window_sum < target:
                window_sum += nums[end]
                end += 1
            if window_sum >= target:
                while window_sum >= target:
                    window_sum -= nums[start]
                    start += 1
                # print("end", end, start)
                if end - start < minimum:
                    minimum = end - start + 1

        if minimum == 10**10000:
            return 0
        else:
            return minimum


test = Solution()
print(test.minSubArrayLen(11, [1, 1, 1, 1, 1]))
