class Solution(object):
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        inc, dec = 1, 1
        res = 1
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                inc = dec + 1
                dec = 1
            elif arr[i] < arr[i - 1]:
                dec = inc + 1
                inc = 1
            else:
                inc = 1
                dec = 1
            res = max(res, inc, dec)
        return res


test = Solution()
print(test.maxTurbulenceSize([0, 1]))
