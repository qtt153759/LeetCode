package main

import (
	"fmt"
)
func main(){
	head:=&ListNode{Val:1,Next:nil}
	tmp:=head
	head.Next=&ListNode{Val:2,Next:nil}
	head=head.Next
	head.Next=&ListNode{Val:0,Next:nil}
	head=head.Next
	head.Next=&ListNode{Val:2,Next:nil}
	head=head.Next
	head.Next=&ListNode{Val:1,Next:nil}
	// head=head.Next
	// head.Next=&ListNode{Val:1,Next:nil}
	fmt.Println("check",isPalindrome(tmp))
}
 type ListNode struct {
     Val int
     Next *ListNode
 }

 // isPalindrome checks whether a Linked List 
// is a palindrome (true) or not (false).
// Uncomment commented print functions to debug.
// The initial linked list is not changed.
// Time: O(n+n+n+n) = O(3n) = O(n)
// Space: O(1)
func isPalindrome(head *ListNode) bool {
	middle := middleNode(head)
	middle = reverseList(middle)
	areEquals := areEquals(head, middle)
	return areEquals	
}


func middleNode(node *ListNode) *ListNode {
	var slow, fast *ListNode = node, node
	for slow != nil && fast != nil && fast.Next != nil {
			slow, fast = slow.Next, fast.Next.Next
	}
	return slow
}


func reverseList(node *ListNode) *ListNode {
	var previous, current *ListNode = nil, node
	for current != nil {
			previous, current, current.Next = current, current.Next, previous
	}
	return previous
}


func areEquals(n1, n2 *ListNode) bool {
	var current1, current2 *ListNode = n1, n2
	for current1 != nil && current2 != nil {
			if current1.Val != current2.Val {
					return false
			}
			current1, current2 = current1.Next, current2.Next
	}
	return true
}




