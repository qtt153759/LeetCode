package main

import "fmt"
func main(){
	fmt.Println(longestCommonPrefix([]string{"ab","a"}))
}
func longestCommonPrefix(strs []string) string {
	res:=""
	if len(strs)==1{
		return strs[0]
	}
	for k:=0;k<len(strs[0]);k++{
		c:=strs[0][k]
    for i:=0;i<len(strs);i++{
			if k==len(strs[i])||strs[i][k]!=c{
				return res
			}
		}
		res+=string(c)
	}
	return res
}