# Definition for a binary tree node.


class TreeNode(object):
    COUNT = [10]

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print2DUtil(self, root, space):

        # Base case
        if root == None:
            return

        # Increase distance between levels
        space += self.COUNT[0]

        # Process right child first
        self.print2DUtil(root.right, space)

        # Print current node after space
        # count
        print()
        for i in range(self.COUNT[0], space):
            print(end=" ")
        print(root.data)

        # Process left child
        self.print2DUtil(root.left, space)

    # Wrapper over print2DUtil()
    def print2D(self, root):

        # space=[0]
        # Pass initial space count as 0
        self.print2DUtil(root, 0)


class Solution(object):
    result = []

    def levelOrder(self, root):
        if root is None:
            return root
        queue = []
        return_list = []
        queue.append(root)
        while len(queue) > 0:
            ans = []
            l = len(queue)
            for l in range(l):
                node = queue.pop(0)
                ans.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            return_list.append(ans)
        return return_list


if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    # root.left = TreeNode(9)
    # root1 = TreeNode(20)
    # root1.left = TreeNode(15)
    # root1.right = TreeNode(7)
    # root.right = root1
    test.levelOrder(root)
