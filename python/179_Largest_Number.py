class Solution(object):
    nums = []

    def largestNumber(self, nums):
        nums = [str(c) for c in nums]
        self.nums = nums
        self.quickSort(0, len(nums) - 1)
        print(self.nums)
        return "0" if self.nums[0] == "0" else "".join(self.nums)

    def quickSort(self, left, right):
        if left >= right:
            return
        index = self.partition(left, right)
        self.quickSort(index + 1, right)
        self.quickSort(left, index - 1)

    def partition(self, left, right):
        for i in range(left, right):
            if self.nums[i] + self.nums[right] > self.nums[right] + self.nums[i]:
                self.nums[i], self.nums[left] = self.nums[left], self.nums[i]
                left = left + 1
        self.nums[left], self.nums[right] = self.nums[right], self.nums[left]
        return left


test = Solution()
print(test.largestNumber([0, 0]))
