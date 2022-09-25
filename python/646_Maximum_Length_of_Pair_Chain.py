class Solution(object):
    def findLongestChain(self, pairs):
        pairs = sorted(pairs, key=lambda x: x[1])
        res = [pairs[0]]
        for i in range(1, len(pairs)):
            if res[-1][1] < pairs[i][0]:
                res.append(pairs[i])
        return len(res)


test = Solution()
print(test.findLongestChain([[1, 2], [7, 8], [4, 5]]))
