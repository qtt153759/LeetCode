class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for i in nums:
            resultPlus = []
            for j in result:
                j = j + [i]
                resultPlus = resultPlus + [j]
            result += resultPlus

        return result


if __name__ == "__main__":
    test = Solution()
    print(test.subsets([1, 2, 3, 4, 5]))
