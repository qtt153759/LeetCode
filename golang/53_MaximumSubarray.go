package main

import "fmt"
func main(){
	fmt.Println("res",maxSubArray([]int{-2,1,-3,4,-1,2,1,-5,4}))
}
func maxSubArray(nums []int) int {
 res:=nums[0]
 current:=nums[0]
 for i:=1;i<len(nums);i++{
	if current<0{
		current=0
	}
	current=current+nums[i]
	
	if res<current{
		res=current
	}
	// fmt.Println("current",current)
 }
 return res
}