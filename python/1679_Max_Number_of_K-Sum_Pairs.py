class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash={}
        count=0
        for num in nums:
            target=k-num
            if hash.get(target,0)==0:
                hash[num]=hash.get(num,0)+1
            else:
                hash[target]=hash[target]-1
                count+=1
        return count
    
sol=Solution()
print(sol.maxOperations(nums = [3,1,3,4,3], k = 6))

