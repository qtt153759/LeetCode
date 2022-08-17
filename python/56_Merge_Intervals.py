class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for n in intervals[1:]:
            if n[0] <= res[-1][1]:
                res[-1][1] = max(n[1], res[-1][1])
            else:
                res.append(n)
        return res
