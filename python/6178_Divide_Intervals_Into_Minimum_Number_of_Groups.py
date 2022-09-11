class Solution(object):
    def minGroups(self, intervals):
        A = []
        for a, b in intervals:
            A.append([a, 1])
            A.append([b + 1, -1])
        res = cur = 0
        for a, diff in sorted(A):
            cur += diff
            res = max(res, cur)
        return res


test = Solution()
print(test.minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]))
