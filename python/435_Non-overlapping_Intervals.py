class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        end, count = float("-inf"), 0
        for interval in sorted(intervals, key=lambda x: x[1]):
            print(interval, end)
            if interval[0] >= end:
                end = interval[1]
                count += 1
        return len(intervals) - count


test = Solution()
print(test.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [-100, -2], [5, 7]]))
