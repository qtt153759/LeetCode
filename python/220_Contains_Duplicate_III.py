class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        d = {}
        w = t + 1
        for i in range(len(nums)):
            v = nums[i] // w
            if v in d:
                print("in", v, d)
                return True
            elif v - 1 in d and abs(d[v - 1] - nums[i]) < w:
                print("less", v - 1, d, w, i)

                return True
            elif v + 1 in d and abs(d[v + 1] - nums[i]) < w:
                print("more", v + 1, d)
                return True
            if i >= k:
                del d[nums[i - k] // w]
            d[v] = nums[i]
        return False


test = Solution()
print(test.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=0, t=0))
