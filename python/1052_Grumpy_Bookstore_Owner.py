class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        res = 0
        statisfied, unsatisfied = 0, 0
        for i in range(minutes):
            statisfied += customers[i] * (1 - grumpy[i])
            unsatisfied += customers[i] * grumpy[i]
        res = unsatisfied + statisfied
        maxUnstatisfied = unsatisfied
        for i in range(minutes, len(customers)):
            statisfied += customers[i] * (1 - grumpy[i])
            unsatisfied += customers[i] * grumpy[i] - customers[i - minutes] * grumpy[i - minutes]
            maxUnstatisfied = max(unsatisfied, maxUnstatisfied)
        return statisfied + maxUnstatisfied


# tong so khach da hai long + so khach lon nhat co the chuyen tu (k0 hai long -> hai long)

test = Solution()
print(test.maxSatisfied([4, 10, 10], [1, 1, 0], 2))
