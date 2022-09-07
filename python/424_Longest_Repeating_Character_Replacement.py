class Solution(object):
    def characterReplacement(self, s, k):
        d = {}
        start = 0
        maxCount = 0
        maxLength = 0
        for end in range(len(s)):
            if s[end] not in d:
                d[s[end]] = 0
            d[s[end]] += 1
            maxCount = max(maxCount, d[s[end]])
            if end - start - maxCount + 1 > k:
                d[s[start]] -= 1
                start += 1
            maxLength = max(maxLength, end - start + 1)
        return maxLength


test = Solution()
print(test.characterReplacement(s="ABAB", k=2))
