class Solution(object):  # co the ap dung bai toan <=k sliding window vao no bang ca
    def numSubarraysWithSum(self, A, S):
        def atMost(S):
            if S < 0:
                return 0
            res = i = 0
            for j in range(len(A)):
                S -= A[j]
                while S < 0:
                    S += A[i]
                    i += 1
                res += j - i + 1
            return res

        return atMost(S) - atMost(S - 1)


test = Solution()
print(test.numSubarraysWithSum(A=[0, 0, 0, 0, 0], S=0))
