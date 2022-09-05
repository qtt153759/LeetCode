class Solution(object):
    def answerQueries(self, nums, queries):
        print(nums)
        nums = sorted(nums)

        tmp = 0
        sum = []
        res = []
        for i in range(len(nums)):
            tmp = tmp + nums[i]
            sum.append(tmp)
        for i in queries:
            res.append(len(sum))
            for j in range(len(sum)):
                if i < sum[j]:
                    res.pop(len(res) - 1)
                    res.append(j)
                    break
        return res


if __name__ == "__main__":
    print("vaa")
    test = Solution()
    print(test.answerQueries(nums=[4, 5, 2, 1], queries=[3, 10, 21]))
