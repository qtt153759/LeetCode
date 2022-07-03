package main

import (
	"fmt"
	"math"
	"sort"
)


func main(){
	fmt.Println("res",threeSumClosest([]int{-1,2,1,-4},1))
}

func threeSumClosest(nums []int, target int) int{
	sort.Ints(nums)
		res:=100000
		var current int
		for i:=0;i<len(nums)-2;i++{
			left:=i+1
			right:=len(nums)-1
			for left<right{
				current= nums[i]+nums[left]+nums[right]
				if math.Abs(float64(target-current))<math.Abs(float64(target-res)){
					res=nums[i]+nums[left]+nums[right]
					// fmt.Println("res",res)
				}
				if current<target {
					left++
					// fmt.Println("narrow left ",i,left,right)
				}else if current>target{
					right--
					// fmt.Println("narrow right ",i,left,right)
				}else{
					return target
				}
			}
		
			
		}
		return res
}
