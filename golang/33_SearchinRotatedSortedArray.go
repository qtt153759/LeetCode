package main

import (
	"fmt"
)
func main(){
	fmt.Println("search",search([]int{3,1},1))
}
//find pivot
func findPivot(nums []int) int{
	left,right:=0,len(nums)-1
	if nums[left]<nums[right]{
		return right
	}
	var mid int
	for left<right{
		mid=(left+right)/2
		if nums[left]<nums[mid]{
			left=mid
		}else if nums[left]>nums[mid]{
			right=mid
		}else{
			return mid
		}
	}
	return left
}
//binary search
func search(nums []int, target int) int {
		if len(nums)==0 || (len(nums)==1&&nums[0]!=target){
			return -1
		}
	
    pivot:=findPivot(nums)
		fmt.Println("pivot",pivot,target,nums[pivot])
		var mid,left,right int
		if nums[pivot]>=target&&target>=nums[0]{
			left=0
			right=pivot
		}else if pivot<len(nums)-1&&nums[pivot+1]<=target&&nums[len(nums)-1]>=target{
			left=pivot+1
			right=len(nums)-1
		}else{
			return -1
		}
		fmt.Println("left,right",left,right)
		for left<right{
			mid=(left+right)/2
			if target==nums[mid]{
				return mid
			}else if target>nums[mid]{
				left=mid+1
			}else{
				right= mid-1
			}
		}

		if nums[left]==target{
			return left
		}
		return -1
}