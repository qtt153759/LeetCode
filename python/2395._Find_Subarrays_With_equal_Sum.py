class Solution(object):
    def findSubarrays(self, nums):
        store = set()
        for i in range(len(nums) - 1):
            tmp = nums[i] + nums[i + 1]
            if tmp in store:
                return True
            store.add(tmp)
        return False


if __name__ == "__main__":
    test = Solution()
    print(test.findSubarrays([1, 2, 3, 4, 5]))
