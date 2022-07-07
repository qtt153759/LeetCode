package main

import (
	"fmt"
)
func main(){
	head:=&ListNode{Val:2,Next:nil}
	tmp:=head
	head.Next=&ListNode{Val:1,Next:nil}
	head=head.Next
	head.Next=&ListNode{Val:3,Next:nil}
	head=head.Next
	head.Next=&ListNode{Val:5,Next:nil}
	head=head.Next
	head.Next=&ListNode{Val:6,Next:nil}
	head=head.Next
	head.Next=&ListNode{Val:4,Next:nil}
	head=head.Next
	head.Next=&ListNode{Val:7,Next:nil}
	print(tmp)

	xyz:=oddEvenList(tmp)
	print(xyz)
}


 type ListNode struct {
     Val int
     Next *ListNode
 }
 //1->3->5
 //2->4-
 
 func oddEvenList(head *ListNode) *ListNode {
		tmp1:=head
		if tmp1 ==nil||tmp1.Next==nil{
			return tmp1
		}
		tmp2:=head.Next
		head2:=head.Next
    for{
			if tmp2.Next!=nil{
				// fmt.Println("check2",tmp1.Val,tmp2.Next.Val)
				tmp1.Next=tmp2.Next
				tmp1=tmp1.Next
			}else{
				tmp1.Next=nil
				break
			}
			if tmp1.Next!=nil{
				tmp2.Next=tmp1.Next
				tmp2=tmp2.Next
			}else{
				tmp2.Next=nil
				break
			}
		}
		tmp1.Next=head2
		return head
}
func print(node *ListNode) {
	var current *ListNode = node
	for current != nil {
			fmt.Printf("%v ", current.Val)
			if current.Next != nil {
					fmt.Print("-> ")
			}
			current = current.Next
	}
	fmt.Println()
	fmt.Println()
}