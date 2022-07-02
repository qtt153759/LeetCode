package main

// func main(){
// 		// nums :=[]int {3,3}
// 		// value:=twoSum(nums,6)
// 		// fmt.Printf("check ",value)
// }
type ListNode struct {
	Val int
	Next *ListNode
}
	
// l1.Next l2.Next != nil sum -> addTwoNumbers(l1.Next,l2.Next) || addTwoNumbers(l1.Next,l2.Next)
// l1 or l2 nil ->  l1.Next+0.5, l1.Next.Next
//l1 l2 nil
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	h:=&ListNode{}
    tmp := h
	for l1 !=nil || l2 != nil{
		if l1 != nil {
			tmp.Val += l1.Val
			l1 = l1.Next
	}
	if l2 != nil {
			tmp.Val += l2.Val
			l2 = l2.Next
	}
	if tmp.Val > 9 {
			tmp.Val -= 10
			tmp.Next = &ListNode{Val: 1}
	} else if l1 != nil || l2 != nil {
			tmp.Next = &ListNode{}
	}
	tmp = tmp.Next
	}
	return h
}