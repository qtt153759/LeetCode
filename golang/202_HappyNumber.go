package main

import (
	"fmt"
	"math"
)
func main(){
	fmt.Println("ishappy",isHappy(19))
}
func isHappy(n int) bool {
	mapIndex:=make(map[int]bool)
  for n>0{
		// fmt.Printf("check",n)
		if mapIndex[n]{
			return false
		}
		if n==1{
			return true
		}
		mapIndex[n]=true
		k:=0
		for n>0{
			k+=int(math.Pow(float64(n%10),2))
			n/=10
		}
		n=k
	}
	return false
}