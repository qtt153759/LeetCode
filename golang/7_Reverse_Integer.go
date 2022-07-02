package main

import (
	"fmt"
	"math"
)
func main(){
	fmt.Printf("result",reverse(-123))//2147483648 
}
func reverse(x int) int {
	res:=0
	for x!=0{
		res=res*10+x%10
		x/=10
	}

	if res>math.MaxInt32||res<math.MinInt32 -1{
		return 0
	}
		return res
}