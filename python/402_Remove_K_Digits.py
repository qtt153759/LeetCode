class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for v in num:
            while len(stack) > 0 and stack[-1] > v and k > 0:
                stack.pop()
                k -= 1
            if len(stack) > 0 or v != "0":
                stack.append(v)
        if k > 0:
            stack = stack[0:-k]
        return "".join(stack)


test = Solution()
print(test.removeKdigits("1432219", 3))
