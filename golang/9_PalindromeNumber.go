package main

import "fmt"
func main(){
		fmt.Print("check",isPalindrome(-323))
}
func isPalindrome(x int) bool {
		if x<0 {return false}
		res:=0
		y:=x
    for y!=0{
			res=res*10+y%10
			y/=10
		}
		return x==res
}