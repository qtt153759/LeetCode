class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        def caculateLength(first, second):
            maxFirst, sumFirst, sumSecond, ans = 0, 0, 0, 0
            for i in range(first + second):
                if i < first:
                    sumFirst += nums[i]
                else:
                    sumSecond = sumSecond + nums[i]
            maxFirst = sumFirst
            ans = sumSecond + maxFirst
            for i in range(first + second, len(nums)):
                sumFirst += nums[i - second] - nums[i - first - second]
                maxFirst = max(sumFirst, maxFirst)
                sumSecond += nums[i] - nums[i - second]
                ans = max(ans, maxFirst + sumSecond)
            return ans

        return max(caculateLength(firstLen, secondLen), caculateLength(secondLen, firstLen))


test = Solution()
print(test.maxSumTwoNoOverlap(nums=[3, 8, 1, 3, 2, 1, 8, 9, 0], firstLen=3, secondLen=2))
