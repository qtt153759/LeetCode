class Solution(object):
    def calculate(self, s):
        result=0
        op="+"
        current=0
        res=0
        for c in s+"+":
            if c.isspace():
                continue
            if c.isdigit():
                current=current*10+ord(c)-ord("0")
                continue
                
            if op=="+":
                res+=current
            elif op=="-":
                res-=current
            elif op=="*":
                res*=current
            else:
                if res//current<0 and res%current != 0:
                    res=res//current+1
                else:
                    res//=current
                print(res)

            if c=="+" or c=="-":
                result+=res
                res=0

            
            op=c 
            current=0             
        
        return result

sol=Solution()
print(sol.calculate("10000-1000/10+100*1"))
print(3//2)
        