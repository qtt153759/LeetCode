package main

import (
	"fmt"
)
func main(){
		fmt.Print("check",maxArea([]int{1,3,2,5,25,24,5}))
}
func maxArea(height []int) int {
	x:=0
	y:=len(height)-1
	res:=0
	// fmt.Println("firs",res)
    for x!=y{
		
			if height[y]>height[x]{
				res=max(res,(y-x)*height[x])
				// fmt.Println("checkasdf",res," heig",height[x],height[y],(y-x-1))
				x++
			}else{
				res=max(res,(y-x)*height[y])
				// fmt.Println("checkasdf",res," heig",height[x],height[y],(y-x-1))

				y--
			}

		}
	return res
}
func max(a int, b int) int{
	if(a>b){
		return a
	}
	return b
}
func min(a int, b int) int{
	if(a>b){
		return b
	}
	return a
}
