class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        d = dict()
        max = 0
        res = []

        for i in range(len(creators)):
            if creators[i] in d:
                if views[i] > views[d[creators[i]][1]]:
                    d[creators[i]][1] = i
                elif views[i] == views[d[creators[i]][1]]:
                    d[creators[i]][1] = i if ids[d[creators[i]][1]] < ids[i] else d[creators[i]][1]
            else:
                d[creators[i]] = [0, i]
            d[creators[i]][0] += views[i]
            if d[creators[i]][0] < max:
                continue
            elif d[creators[i]][0] > max:
                max = d[creators[i]][0]
                res = []
            res.append([creators[i], ids[d[creators[i]][1]]])
        return res


test = Solution()
print(test.mostPopularCreator(["a", "a"], ["aa", "a"], [5, 5]))
