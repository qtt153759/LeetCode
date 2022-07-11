package main

func main() {

}

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, targetSum int) int {
	parentSums := make(map[int]uint32, 0)
	res := visit(root, parentSums, 0, targetSum)
	return int(res)
}

func visit(node *TreeNode, parentSums map[int]uint32, curr, target int) uint32 {
	if node == nil {
		return 0
	}
	curr += node.Val
	res := parentSums[curr-target]
	if curr == target {
		res++
	}
	parentSums[curr]++
	left := visit(node.Left, parentSums, curr, target)
	right := visit(node.Right, parentSums, curr, target)
	parentSums[curr]--
	return res + left + right
}
