from collections import Counter


class Solution:
    def robotWithString(self, s):
        dic, t, ans = Counter(s), [], []
        for char in s:
            t.append(char)
            if dic[char] == 1:
                del dic[char]
            else:
                dic[char] -= 1
            while dic and t and min(dic) >= t[-1]:
                ans += t.pop()
        ans += t[::-1]
        return "".join(ans)


test = Solution()
print(test.robotWithString("cdbacb"))
