class Solution(object):
    def balancedString(self, s):
        d = {"Q": 0, "W": 0, "R": 0, "E": 0}
        k = len(s) / 4
        for i in s:
            d[i] += 1
        left = 0
        n = len(s)
        res = n
        for right in range(len(s)):
            d[s[right]] -= 1
            while left < n and d["Q"] <= k and d["W"] <= k and d["R"] <= k and d["E"] <= k:
                res = min(res, right - left + 1)
                d[s[left]] += 1
                left += 1
        return res


# y tuong don gian la tinh min window that khi mk bo no di thi tat ca cac gia tri con lai deu <=len(s)/4
# vi thuc te thi chung ta co dieu chinh tat ca cac ky tu trong window de no bien tat ca thoa man =len(s)/4
# tai sao trong bai toan window function, dk left<=right ko thuc su hieu qua vi khi left=righ+1 thi window fuction vo nghia
# ma neu widow vo nghia=> quay ve dang problem=> ma problem luon ko thoa man
test = Solution()
print(test.balancedString("RQWE"))
