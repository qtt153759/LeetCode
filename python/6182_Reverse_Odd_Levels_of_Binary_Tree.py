# Definition for a binary tree node.
from binaryTree import *


class Solution(object):
    def reverseOddLevels(self, root):
        return self.bfs(root)

    def bfs(self, root):
        queue = [root]
        valQueue = [root.val]
        isReverse = True
        while len(queue):
            valQueue = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    valQueue.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    valQueue.append(node.right.val)
            if isReverse:
                l1 = len(valQueue)
                for i in range(l1):
                    queue[i].val = valQueue[l1 - 1 - i]
            isReverse = not isReverse
        return root


root = TreeNode(2)
root1 = TreeNode(3)
root2 = TreeNode(5)
root.left = root1
root.right = root2
root1.left = TreeNode(8)
root1.right = TreeNode(15)
root2.left = TreeNode(21)
root2.right = TreeNode(34)
root.display()
test = Solution()
test.reverseOddLevels(root).display()
