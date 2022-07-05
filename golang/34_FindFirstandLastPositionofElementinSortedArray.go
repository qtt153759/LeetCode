package main

import "fmt"
func main(){
	fmt.Println("res",searchRange([]int{1,2,3},2))
}
func searchRange(nums []int, target int) []int {
		if(len(nums)==0)||nums[0]>target||nums[len(nums)-1]<target{
			return []int{-1,-1}
		}
		k :=-1
		left:=0
		right:=len(nums)-1
    for left<right{
			mid:=(left+right)/2
			if nums[mid]==target{
				k=mid
				break
			}else if nums[mid]>target{
				right=mid-1
			}else{
				left=mid+1
			}
		}
		if k==-1{
			if nums[left]!=target{
				return []int{-1,-1}
			}else{
				k=left
			}
		}
		// fmt.Println("k",k)
		i:=0
		first:=k
		last:=k
		for k+i<len(nums){
			if k+i+1<len(nums)&&nums[k+i+1]==nums[k+i]{
				i++
				continue
			}
			last=k+i
			i=0
			break
		}
		for k-i>=0{
			if k-i-1>=0&&nums[k-i]==nums[k-i-1]{
				i++
				continue
			}
			first=k-i
			break
		}
		return []int{first,last}
}