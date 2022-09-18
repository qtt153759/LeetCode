class Solution(object):
    def smallestEvenMultiple(self, n):
        if n % 2:
            return 2 * n
        return n


test = Solution()
print(test.smallestEvenMultiple(2))
