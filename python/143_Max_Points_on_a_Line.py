class Solution(object):
    def maxPoints(self, points):
        countPoint={}
        max=0
        for i in range(len(points)-1):
            countPoint={}
            for j in range(i+1,len(points)):
                x1,y1=points[i]
                x2,y2=points[j]
                diffY=y1-y2
                diffX=x1-x2
                if diffX==0:
                    a,b=x1,float('inf')
                elif diffY==0:
                    a,b=0,y1
                else:
                    a=diffY/diffX
                    b=y1-a*x1
                # print(points[i],points[j],(a,b))
                countPoint[(a,b)]=countPoint.get((a,b), 0)+1
                if countPoint[(a,b)]>max-1:
                    max=countPoint[(a,b)]
        return max+1
sol=Solution()
print(sol.maxPoints([[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]))
        