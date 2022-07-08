package main

import (
	"fmt"
)
func main(){
	fmt.Println("check",longestPalindrome([]string{"ab","ty","yt","lc","cl","ab"}))
}
func longestPalindrome(words []string) int {
		store:=make(map[string]int)
		res:=0
    for _,word:=range words{
			reverseWord:=string(word[1])+string(word[0])
			// fmt.Println("check",reverseWord)
			if store[reverseWord]>0 {
				store[reverseWord]--
				res+=4
			}else{
				store[word]++
			}
		}
		for i:='a';i<='z';i++{
			if store[fmt.Sprintf("%c%c", i, i)]>0 {
				res+=2
				break
			}
		}
		return res
}