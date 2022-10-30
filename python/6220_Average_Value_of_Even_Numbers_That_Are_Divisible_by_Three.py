class Solution(object):
    def averageValue(self, nums):
        total, count = 0, 0
        for num in nums:
            if num % 6 == 0:
                count += 1
                total += num

        return total / count if count != 0 else 0


test = Solution()
print(test.averageValue([1, 2, 4, 7, 10]))
