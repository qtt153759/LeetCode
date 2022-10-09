class Solution(object):
    def hardestWorker(self, n, logs):
        result = [logs[0][0], logs[0][1]]
        for i in range(1, len(logs)):
            # print(logs[i][1] - logs[i - 1][1])
            if (logs[i][1] - logs[i - 1][1]) > result[1]:
                result = [logs[i][0], logs[i][1] - logs[i - 1][1]]
            elif logs[i][1] - logs[i - 1][1] == result[1] and result[0] > logs[i][0]:
                result = [logs[i][0], logs[i][1] - logs[i - 1][1]]
        return result[0]


test = Solution()
print(test.hardestWorker(70, [[36, 3], [1, 5], [12, 8], [25, 9], [53, 11], [29, 12], [52, 14]]))
