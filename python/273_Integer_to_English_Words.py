# class Solution(object):
#     def numberToWords(self, num):
#         smallNumber=["Zero","One","Two","Three","Four","Five","Six","Seven",
#                      "Eight","Nine","Ten","Eleven","Twelve","Thirteen",
#                      "Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
#         midNumber= ["Zero","Ten","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

#         def subNumberToWords(num):
#             res=""
#             large=num//100
#             mid=num-large*100
#             small=num%10
#             if num==0:
#                 return smallNumber[0]
#             if large>0:
#                 res+=smallNumber[large]+" Hundred "
#             if mid==0:
#                 return res
#             if mid<20:
#                 res+=smallNumber[mid]+ " "
#                 return res
#             mid=mid//10
#             print(mid)
#             res+=midNumber[mid]+" "
#             if small>0:
#                 res+=smallNumber[small]+ " "
#             return res
        
#         result=""
#         for i,postfix in zip([3,2,1,0],["Billion ","Million ","Thousand ",""]):
#             val=num//pow(1000,i)
#             value=subNumberToWords(val)
#             if value!="Zero":
#                 result+=subNumberToWords(val)+postfix
#             num=num-val*pow(1000,i)
#         return result


class Solution(object):
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n/10-2]] + words(n%10)
            if n < 1000:
                return [to19[n/100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return words(n/1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'


sol=Solution()  
print(sol.numberToWords(1100))