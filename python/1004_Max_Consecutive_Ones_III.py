class Solution(object):
    class Solution(object):
        def longestOnes(self, A, K):
            i = 0
            for j in range(len(A)):
                K -= 1 - A[j]
                if K < 0:
                    K += 1 - A[i]
                    i += 1
            return j - i + 1


# cai technique nay rat hay, loi dung K la bien current luon compare no vs 0 la dc
# cai sliding window nay la right luc nao cx +1, con left chi +1 khi k<0
# khong can ton cong tao while loop cho left lam gi boi vi res max da bang right-left+1 roi

test = Solution()
print(test.longestOnes(nums=[0], k=0))
