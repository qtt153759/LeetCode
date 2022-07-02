package main

import (
	"fmt"
)

var e = [][]string{
	{"I","V","X"},{"X","L","C"},{"C","D","M"},{"M"},
}

var d= [][]uint8{
	{0},{0,0},{0,0,0},{0,1},{1},{1,0},{1,0,0},{1,0,0,0},{0,2},
}
func main(){
	fmt.Println("res",intToRoman(90))
}
func intToRoman(num int) string {
    res:=""
		i:=0
		for num>0{
			res=covert(num%10,i)+res
			i++
			num/=10
		}
		return res

}
func covert(num int,k int) string{
	if num ==0 {
		return ""
	}
	res:=""
	for _,val := range d[num-1]{
		res+=e[k][val]
	}
	return res
}