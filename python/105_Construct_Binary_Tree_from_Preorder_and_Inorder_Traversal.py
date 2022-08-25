# Definition for a binary tree node.
from binaryTree import *


class Solution(object):
    preorder = []
    indexPreorder = 0

    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        return self.travelTree(inorder)

    def travelTree(self, subsetInorder):
        partition = subsetInorder.index(self.preorder.pop(0))
        tmp = TreeNode(subsetInorder[partition])
        leftSubsetInorder = subsetInorder[:partition]

        rightSubsetInorder = subsetInorder[partition + 1 :]
        if len(leftSubsetInorder) > 0:
            tmp.left = self.travelTree(leftSubsetInorder)
        if len(rightSubsetInorder) > 0:
            tmp.right = self.travelTree(rightSubsetInorder)
        return tmp


if __name__ == "__main__":
    test = Solution()
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root1 = TreeNode(20)
    # root1.left = TreeNode(15)
    # root1.right = TreeNode(7)
    # root.right = root1
    # print2D(root)
    # print("============")
    test.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]).display()
