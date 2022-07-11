package main

func main() {

}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	_, res := checkHeight(root)
	return res
}
func checkHeight(root *TreeNode) (int, bool) {
	if root == nil {
		return 0, true
	}
	left, isLeftBalanced := checkHeight(root.Left)
	if isLeftBalanced == false {
		return 0, false
	}
	right, isRightBalanced := checkHeight(root.Right)
	if isRightBalanced == false {
		return 0, false
	}
	if right >= left && right-left <= 1 {
		return right + 1, true
	} else if left > right && left-right <= 1 {
		return left + 1, true
	}
	return 0, false
}
