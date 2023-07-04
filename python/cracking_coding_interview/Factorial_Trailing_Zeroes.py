class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=5
        sum=0
        while(i<=n):
            sum=n/i+sum
            i=i*5
            
        return sum

sol=Solution()  
print(sol.trailingZeroes(0))