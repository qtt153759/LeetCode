package main

import (
	"fmt"
	"math"
)

func main() {
	head := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val:   2,
			Left:  nil,
			Right: nil,
		},
		Right: nil,
	}
	fmt.Println("int", diameterOfBinaryTree(head))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var maxDiameter = 0

func diameterOfBinaryTree(root *TreeNode) int {
	checkHeight(root)
	return maxDiameter
}
func checkHeight(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := checkHeight(root.Left)
	// fmt.Println("left ",root.Val,left)
	right := checkHeight(root.Right)
	// fmt.Println("right ",root.Val,right)
	if left+right > maxDiameter {
		// fmt.Println("update ", root.Val, right, left, maxDiameter)
		maxDiameter = left + right
	}
	return int(1 + math.Max(float64(left), float64(right)))
}
