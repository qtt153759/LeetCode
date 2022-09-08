class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        phash = {}
        shash = {}
        m = len(s)
        n = len(p)
        if m < n:
            return False
        for i in range(n):
            if p[i] in phash:
                phash[p[i]] += 1
            else:
                phash[p[i]] = 1
            if s[i] in shash:
                shash[s[i]] += 1
            else:
                shash[s[i]] = 1
        if shash == phash:
            return True
        for i in range(0, m - n):

            if shash[s[i]] == 1:
                del shash[s[i]]
            else:
                shash[s[i]] -= 1
            if s[i + n] in shash:
                shash[s[i + n]] += 1
            else:
                shash[s[i + n]] = 1
            if len(shash) == len(phash) and shash == phash:
                return True
        return False


test = Solution()
print(test.checkInclusion("ab", "eidboaoo"))
