class Solution(object):
    def findMinArrowShots(self, points):
        points = sorted(points, key=lambda x: x[0])

        res = [points[0]]
        print(res)
        for i in range(1, len(points)):
            print("xet", points[i], " vs ", res)
            if res[-1][0] <= points[i][0] and points[i][0] <= res[-1][1]:
                tmp = min(res[-1][1], points[i][1])
                res[-1] = [points[i][0], tmp]
                continue
            res.append(points[i])
        return len(res)


test = Solution()
print(test.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
