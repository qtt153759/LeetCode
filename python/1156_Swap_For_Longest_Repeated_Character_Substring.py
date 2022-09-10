class Solution(object):
    def maxRepOpt1(self, text):
        interval = []
        count = {}
        tmp = [text[0], 1]
        res = 0
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                tmp[1] += 1
                continue
            interval.append(tmp)
            if tmp[0] not in count:
                count[tmp[0]] = 0
            count[tmp[0]] += tmp[1]
            tmp = [text[i], 1]
        interval.append(tmp)
        if tmp[0] not in count:
            count[tmp[0]] = 0
        count[tmp[0]] += tmp[1]
        for c, k in interval:
            res = max(res, min(k + 1, count[c]))
        for i in range(1, len(interval) - 1):
            if interval[i][1] == 1 and interval[i - 1][0] == interval[i + 1][0]:
                res = max(res, min(interval[i - 1][1] + interval[i + 1][1] + 1, count[interval[i - 1][0]]))
        return res


test = Solution()
print(test.maxRepOpt1("aaaaa"))
