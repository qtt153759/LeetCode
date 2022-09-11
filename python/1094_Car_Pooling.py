class Solution(object):
    def carPooling(self, trips, capacity):
        location = []
        for i in range(len(trips)):
            location.append([-trips[i][0], trips[i][1]])
            location.append([trips[i][0], trips[i][2]])
        location = sorted(location, key=lambda x: (x[1], -x[0]))
        for i in range(len(location)):
            capacity += location[i][0]
            if capacity < 0:
                return False
        return True


test = Solution()
print(test.carPooling([[4, 5, 6], [6, 4, 7], [4, 3, 5], [2, 3, 5]], 13))
