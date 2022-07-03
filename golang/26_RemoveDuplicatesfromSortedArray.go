package main

import (
	"fmt"
)
func main(){
	fmt.Println("check",removeDuplicates([]int{0,0,1,1,1,2,2,3,3,4}))
}
func removeDuplicates(nums []int) int {
		if len(nums)<2{
			return len(nums)
		}
		j:=1
		for i:=1;i<len(nums);i++{
			if nums[i]==nums[i-1]{
				nums[j]=nums[i]
				j++
			}
		}
		// fmt.Println("ok",nums)
		return j
}