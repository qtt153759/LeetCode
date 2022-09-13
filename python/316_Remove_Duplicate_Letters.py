class Solution(object):
    def increasingTriplet(self, nums):
        first, second = float("inf"), float("inf")
        for v in nums:
            if v <= first:
                first = v
            elif v <= second:
                second = v
            else:
                return True
        return False


# y tuong dung first va second. Muc tieu chinh neu tim dc 1 so lon hon second thi co
# nghia la so do thoa man v>second>first.=> can cap nhat lien tuc first va second
test = Solution()
print(test.increasingTriplet([1, 1, 1, 1]))
