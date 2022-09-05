class Solution(object):
    def checkDistances(self, s, distance):
        a = ord("a")
        for i in range(len(s)):
            b = ord(s[i])
            c = distance[b - a]
            if c == -1:
                continue
            if i + c + 1 > len(s) - 1 or s[i] != s[i + c + 1]:
                return False
            distance[b - a] = -1
        return True


if __name__ == "__main__":
    test = Solution()
    print(test.checkDistances("abcabc", [0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
