# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """

        if not root:
            return None
        cur = root
        nextLevel = root.left

        while cur.left:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = nextLevel
                nextLevel = cur.left


if __name__ == "__main__":
    test = Solution()
    root = Node(1)
    root1 = Node(2)
    root2 = Node(3)
    root1.left = Node(4)
    root1.right = Node(5)
    root2.left = Node(6)
    root2.right = Node(7)

    root.left = root1
    root.right = root2
    root = test.connect(root)
    tmp = root
    ans = []
    while tmp:
        tmp1 = tmp
        while tmp1:
            print(tmp1.val)
            ans.append(tmp1.val)
            tmp1 = tmp1.next
        ans.append("#")
        tmp = tmp.left
    print(ans)
