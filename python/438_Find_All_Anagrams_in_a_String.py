from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        phash = {}
        shash = {}
        m = len(s)
        n = len(p)
        if m < n:
            return []
        result = []
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
            result.append(0)
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
                result.append(i + 1)
        return result


test = Solution()
print(test.findAnagrams("abab", p="ab"))
