class Solution(object):
    def totalFruit(self, fruits):

        left = 0
        basket = {}
        res = 0
        for right in range(0, len(fruits)):
            if fruits[right] not in basket:
                basket[fruits[right]] = 1
            else:
                basket[fruits[right]] += 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            res = max(res, right - left + 1)
        return res


test = Solution()
print(test.totalFruit([1, 2, 3, 2, 2]))
