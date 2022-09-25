class Solution(object):
    def sortPeople(self, names, heights):
        n = len(names)
        for i in range(n):
            names[i] = [names[i], heights[i]]
        names = sorted(names, key=lambda x: -x[1])
        return [x[0] for x in names]


test = Solution()
print(test.sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))
