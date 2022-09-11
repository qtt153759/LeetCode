class Solution(object):
    def corpFlightBookings(self, bookings, n):
        res = [0] * (n + 1)
        for i, j, k in bookings:
            res[i - 1] += k
            res[j] -= k
        for i in range(1, n):
            res[i] += res[i - 1]
        return res[:-1]


test = Solution()
print(test.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))
