class Solution(object):
    def partitionString(self, s):
        d = {}
        res = 1
        for right in range(len(s)):
            if s[right] not in d:
                d[s[right]] = True
                continue
            d = {s[right]: True}
            res = res + 1

        return res


test = Solution()
print(test.partitionString(s="ssssss"))
