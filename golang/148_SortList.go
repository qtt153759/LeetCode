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
	xyz:=sortList(tmp)
	print(xyz)
}
type ListNode struct {
	Val int
	Next *ListNode
}
func sortList(head *ListNode) *ListNode {
		// fmt.Println("sort in")
		// print(head)
		// time.Sleep(1*time.Second)

    if head==nil || head.Next==nil{
			return head
		}
		slow:=head
		fast:=head
		for fast.Next !=nil&&fast.Next.Next!=nil{
			slow=slow.Next
			fast=fast.Next.Next
		}
		tmp:=slow
		slow=slow.Next
		tmp.Next=nil
		// fmt.Println("check l1")
		l1:=sortList(head)
		// fmt.Println("check l2")

		l2:=sortList(slow)
		l:=mergeSort(l1,l2)
		
		// fmt.Println("sort out")
		// print(l)
		// time.Sleep(1*time.Second)
		return l
}
func mergeSort(l1 *ListNode,l2 *ListNode)*ListNode{
	l:=&ListNode{}
	ptr:=l
	for l1!=nil && l2!=nil{
		if l1.Val<l2.Val{
			l.Next=l1
			l1=l1.Next
		}else{
			l.Next=l2
			l2=l2.Next
		}
		l=l.Next
	}
	for l1 !=nil{
		l.Next=l1
		l1=l1.Next
		l=l.Next
	}
	for l2 !=nil{
		l.Next=l2
		l2=l2.Next
		l=l.Next
	}
	ptr=ptr.Next
	return ptr
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