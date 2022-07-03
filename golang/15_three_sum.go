package main

import (
	"fmt"
	"sort"
)


func main(){
	fmt.Println("res",threeSum([]int{-1,1,-1,0}))
}

func threeSum(nums []int) [][]int {
		sort.Ints(nums)
		res:=[][]int{}
		for i:=0;i<len(nums)-2;i++{
			left:=i+1
			right:=len(nums)-1
			if i>0 && nums[i]==nums[i-1]{
				fmt.Print("i",i)
				continue
			}
			fmt.Println("new i",i,len(nums)-2)

			for left<right{
				fmt.Println("i ",i,left,right, "voi",nums[i],nums[left],nums[right])
				
				if nums[i]+nums[left]+nums[right]==0{
					res=append(res, []int{nums[i],nums[left],nums[right]})
					left++
				  right--
					fmt.Println("bang ",i,left,right)
					for nums[left-1]==nums[left] && left < right{
						left++
						fmt.Println("same trai ",i,left,right)
	
					}
					for right<len(nums)-1 && nums[right+1]==nums[right] && left < right{
						right--
						fmt.Println("same phai ",i,left,right)
	
					}

				}else if nums[i]+nums[left]+nums[right]<0 && left < right{
					left++
					fmt.Println("narrow left ",i,left,right)
				}else{
					right--
					fmt.Println("narrow right ",i,left,right)

				}
			fmt.Println("out")
				

			}
		}
		return res
}