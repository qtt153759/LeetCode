package main

import (
	"fmt"
)
type ListNode struct {
	Val int
	Next *ListNode
}
 
func main(){
	head:=&ListNode{Val:1,Next:nil}
	tmp:=head
	// head.Next=&ListNode{Val:2,Next:nil}
	// head=head.Next
	// head.Next=&ListNode{Val:3,Next:nil}
	// head=head.Next
	// head.Next=&ListNode{Val:4,Next:nil}
	// head=head.Next
	// head.Next=&ListNode{Val:5,Next:nil}
	fmt.Println("ok")
	fmt.Println("check",removeNthFromEnd(tmp,1))
}

 
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	tmp:=head
	for i:=0;i<n;i++{
		// fmt.Println("i",tmp.Val)
		tmp=tmp.Next
		// fmt.Println("xong")
	}
	// fmt.Println("fu")
	if tmp==nil{
		return head.Next
	}
	here:=head
	for tmp.Next !=nil{
		// fmt.Println("half i",tmp.Val,here.Val)
		tmp=tmp.Next
		here=here.Next
	}
	here.Next=here.Next.Next
	// fmt.Println("half",here.Val,here.Next.Val)
	return head
}