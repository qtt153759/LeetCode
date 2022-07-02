package main

import (
	"fmt"
)
func main(){
	fmt.Printf("result",lengthOfLongestSubstring("aabaab!bb"))
}
func lengthOfLongestSubstring(s string) int {
	indexMap:=make(map[uint8]int)
	start:=0
	result:=0
  for i:=0;i<len(s);i++{
		duplicateIndex, isDuplicate := indexMap[s[i]]
		fmt.Println("yes",isDuplicate,"position",duplicateIndex,s[i])
		if isDuplicate{
			for j:=start;j<=duplicateIndex;j++{
				delete(indexMap,s[j])
			}
			if result < (i-start){
				result=(i-start)
				fmt.Println("v",result)
			}
			start=duplicateIndex+1
		}
		indexMap[s[i]]=i
		fmt.Println("set",indexMap[s[i]])
	}
	if result < (len(s)-start){
		result=(len(s)-start)
	}
	return result
}