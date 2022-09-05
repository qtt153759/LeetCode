class Solution(object):
    def removeStars(self, s):
        res = []
        for c in s:
            if c == "*":
                res.pop(len(res) - 1)
            else:
                res.append(c)
        result = ""
        for i in res:
            result = result + i
        return result


if __name__ == "__main__":
    test = Solution()
    print(test.removeStars("erase*****"))
