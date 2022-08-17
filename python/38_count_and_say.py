class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        res = "1"
        for x in range(2, n + 1):
            cur, count, s = 0, 0, ""
            for i in range(len(res)):
                if res[cur] == res[i]:
                    count = count + 1
                else:
                    s += str(count) + res[cur]
                    cur = i
                    count = 1
            s += str(count) + res[len(res) - 1]
            res = s

        return res


if __name__ == "__main__":
    test = Solution()
    print(test.countAndSay(5))
