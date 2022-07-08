package main

import "fmt"
func main(){
	fmt.Println(leastInterval([]byte{'A','A','A','B','B','B'},2))
}
func leastInterval(tasks []byte, n int) int {
	maxCnt, numberWithMaxCount := 0, 0
	m := map[byte]int{}
	for _, t := range tasks {
			m[t]++
			if m[t] > maxCnt {
					maxCnt = m[t]
					numberWithMaxCount = 1
			} else if m[t] == maxCnt {
					numberWithMaxCount++
			}
	}
	candidate := (maxCnt-1) * (n+1) + numberWithMaxCount
	if candidate <= len(tasks) {
			return len(tasks)
	} else {
			return candidate
	}
}