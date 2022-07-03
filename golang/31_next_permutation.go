package main

import "fmt"

// import "fmt"
func main(){
	nums:=[]int{2,3,1}
	nextPermutation(nums)
	// fmt.Println("nums",nums)
}
func nextPermutation(nums []int)  {
		var idx int
    for i:=len(nums)-1;i>0;i--{
			// fmt.Println("i",i)
			if(nums[i]>nums[i-1]){
				idx=i-1
				find:=binarySearch(nums,i,len(nums)-1,nums[idx])
				nums[idx],nums[find]=nums[find],nums[idx]
				reverseArray(nums,i,len(nums)-1)
				return
			}
		}
		// fmt.Print("none")
		reverseArray(nums,0,len(nums)-1)
		// fmt.Println("nums",nums)

		return
}
func binarySearch(nums[]int,left int, right int,target int)int{
	// fmt.Println("search",left,right,target)
	if(nums[right]>target){
		return right
	}

	for left<right{
		mid:=(left+right)/2
		// fmt.Println("mid",mid,left,right,target,nums[left],nums[right])
		if left==mid {
			return left
		}
		if target>=nums[mid]{
			right=mid
		}else	if target<nums[mid] {
			left=mid
		}
	}
	return left
}
func reverseArray(nums []int,left int,right int){
	// fmt.Println("nums",nums,left,right)

	for i:=0;i<=(right-left)/2;i++{
		nums[left+i],nums[right-i]=nums[right-i],nums[left+i]
		fmt.Println("swapt",nums[left+i],nums[right-i],left+i,right-i)

	}
	// fmt.Println("nums",nums)

}
